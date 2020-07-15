from django.shortcuts import render_to_response,get_object_or_404  #不使用render，改使用render_to_response
from .models import Blog,BlogType
from django.conf import settings
from django.core.paginator import Paginator

#each_page_blogs_number = settings.EACH_PAGE_BLOGS_NUMBER  #分页页码

def get_blog_list_common_data(request, blogs_all_list):
    paginator = Paginator(blogs_all_list, settings.EACH_PAGE_BLOGS_NUMBER) #每settings.EACH_PAGE_BLOGS_NUMBER篇分一页
    # request.GET是一个字典，所以可以使用get方法
    # 获取页码参数（GET请求）
    page_num = request.GET.get('page' ,1) #查看page传递的值，如果没有，就设定默认为1
    page_of_blogs = paginator.get_page(page_num) #get_page()函数会自动判断page_num传递的参数，如果超出范围或其他不符合的情况不会处理
    currentr_page_num = page_of_blogs.number #获取当前页码
    # 获取当前页码前后各2页的页码范围
    page_range = list(range(max(currentr_page_num -2, 1), currentr_page_num)) +  \
                 list(range(currentr_page_num, min(currentr_page_num + 2,paginator.num_pages) +1 ))
                                                                            # \ 代表换行  最后+1是因为range()左闭右开
    # 加上省略页码
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    # 加上首页1和尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)   # 使用insert()在list里增加数据，第一个参数0表示在list中的0位增加数据，第二个参数1表示增加的数据为数字1
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)  # 在list最后增加，使用append()
    context = {}   
    context['blogs'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
    context['page_range'] = page_range
    context['blog_types'] = BlogType.objects.all()
    #context['blogs_count'] = Blog.objects.all().count()
    context['blog_dates'] = Blog.objects.dates('created_time','month', order='DESC')  # 按月份归档  ASC升序，DESC降序
    return context

def blog_list(request):
    blogs_all_list = Blog.objects.all()
    context = get_blog_list_common_data(request, blogs_all_list)
    return render_to_response('blog/blog_list.html',context)

def blogs_with_type(request,blog_type_pk):  #blog_type_pk是来自blog/urls.py中第二个path传递的数字
    blog_type = get_object_or_404(BlogType,pk=blog_type_pk)
    blogs_all_list = Blog.objects.filter(blog_type=blog_type)
    context = get_blog_list_common_data(request, blogs_all_list)
    context['blog_type'] = blog_type
    return render_to_response('blog/blogs_with_type.html',context)

def blogs_with_date(request, year, month):
    blogs_all_list = Blog.objects.filter(created_time__year=year,created_time__month=month)  # 找到符合我们传入年月的博客列表
    context = get_blog_list_common_data(request, blogs_all_list)
    context['blogs_with_date'] = '%s年%s月' % (year,month)
    return render_to_response('blog/blogs_with_date.html',context)

def blog_detail(request,blog_pk):
    context = {}
    blog = get_object_or_404(Blog, pk=blog_pk)
    context['blog'] = blog
    context['previous_blog'] = Blog.objects.filter(created_time__gt=blog.created_time).last()  #取创建时间比当前博客大的博客列表中的最后一条
    context['next_blog'] = Blog.objects.filter(created_time__lt=blog.created_time).first()  #取创建时间比当前博客小的博客列表中的第一条｜可以将first()替换为[0]进行切片
    return render_to_response('blog/blog_detail.html',context)