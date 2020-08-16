import datetime
from django.shortcuts import render, redirect
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db.models import Sum
from django.core.cache import cache
from django.contrib import auth
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import JsonResponse

from read_statistics.utils import get_seven_days_read_data, get_today_hot_data, get_yesterday_hot_data
from blog.models import Blog
from .forms import LoginForm, RegForm

def get_7_days_hot_blogs():
    today = timezone.now().date()
    date = today - datetime.timedelta(days=7)
    blogs = Blog.objects \
                .filter(read_details__date__lt=today, read_details__date__gte=date) \
                .values('id', 'title') \
                .annotate(read_num_sum=Sum('read_details__read_num')) \
                .order_by('-read_num_sum')
    return blogs[:7]

def home(request):
    blog_content_type = ContentType.objects.get_for_model(Blog)
    dates, read_nums = get_seven_days_read_data(blog_content_type)


    # 获取7天热门博客的缓存数据
    hot_blogs_for_7_days = cache.get('hot_blogs_for_7_days')
    if hot_blogs_for_7_days is None:
        hot_blogs_for_7_days = get_7_days_hot_blogs()
        cache.set('hot_blogs_for_7_days', hot_blogs_for_7_days, 3600)  #最后一个为有效期（秒）
        print('calc')
    else:
        print('use cache')

    context = {}
    context['read_nums'] = read_nums
    context['dates'] = dates
    context['today_hot_data'] = get_today_hot_data(blog_content_type)
    context['yesterday_hot_data'] = get_yesterday_hot_data(blog_content_type)
    context['hot_blogs_for_7_days'] = get_7_days_hot_blogs()
    return render(request, 'home.html',context)

def login(request):
    if request.method == 'POST':  
    # 如果请求中的提交方法为POST，则提交POST中request的内容，否则渲染页面
        login_form = LoginForm(request.POST) # request.POST中包含了username等键值对
        # login_form = LoginForm({'username':'sss'}) 
        if login_form.is_valid():  # 判断login_form是否有效，并进行forms.py中的clean方法
            user = login_form.cleaned_data['user']
            auth.login(request, user)  # 登录
            return redirect(request.GET.get('from', reverse('home'))) 
            # redirect表示进行重定向 进行页面跳转，跳转到原来的页面，
            # 利用在HTML模板文件中添加GET请求参数?from=，将之前的页面地址传递过来，如果没有则返回首页
    
    else:
        login_form = LoginForm()

    context = {}
    context['login_form'] = login_form # 如果错误，此时login_form携带了上面增加的错误信息
    return render(request, 'login.html', context)

def login_for_modal(request):
    login_form = LoginForm(request.POST)
    data = {}
    if login_form.is_valid():  
        user = login_form.cleaned_data['user']
        auth.login(request, user)  
        data['status'] = 'SUCCESS'
    else:
        data['status'] = 'ERROR'
    return JsonResponse(data)


def register(request):
    if request.method == 'POST':  
        reg_form = RegForm(request.POST)
        if reg_form.is_valid():
            username = reg_form.cleaned_data['username']
            email = reg_form.cleaned_data['email']
            password = reg_form.cleaned_data['password']
            # 创建一个新的用户
            user = User.objects.create_user(username, email, password) 
            user.save()
            # 登录用户
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            # 跳转到注册钱的页面
            return redirect(request.GET.get('from', reverse('home'))) 
            '''
            # 通过实例化进行创建用户
            user = User()
            user.username = username
            user.email = email
            user.set_password(password)  #因为要保存的是加密过后的密码不是明文的密码，所以要使用set_password方法
            user.save()
            '''
    else:
        reg_form = RegForm()

    context = {}
    context['reg_form'] = reg_form
    return render(request, 'register.html', context)