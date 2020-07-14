from django.shortcuts import render_to_response,get_object_or_404  #不使用render，改使用render_to_response
from .models import Blog,BlogType
from django.core.paginator import Paginator

def blog_list(request):
    blogs_all_list = Blog.objects.all()
    paginator = Paginator(blogs_all_list, 10) #每10个分一页
    # request.GET是一个字典，所以可以使用get方法
    # 获取页码参数（GET请求）
    page_num = request.GET.get('page' ,1) #查看page传递的值，如果没有，就设定默认为1
    page_of_blogs = paginator.get_page(page_num) #get_page()函数会自动判断page_num传递的参数，如果超出范围或其他不符合的情况不会处理

    context = {}
    context['blogs_all_list'] = blogs_all_list
    context['page_of_blogs'] = page_of_blogs
    context['blog_types'] = BlogType.objects.all()
    #context['blogs_count'] = Blog.objects.all().count()
    return render_to_response('blog/blog_list.html',context)

def blog_detail(request,blog_pk):
    context = {}
    context['blog'] = get_object_or_404(Blog, pk=blog_pk)
    return render_to_response('blog/blog_detail.html',context)

def blogs_with_type(request,blog_type_pk):  #blog_type_pk是来自blog/urls.py中第二个path传递的数字
    context = {}
    blog_type = get_object_or_404(BlogType,pk=blog_type_pk)
    context['blog_type'] = blog_type
    context['blogs'] = Blog.objects.filter(blog_type=blog_type)
    context['blog_types'] = BlogType.objects.all()
    return render_to_response('blog/blogs_with_type.html',context)
