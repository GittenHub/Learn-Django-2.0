from django.shortcuts import render_to_response,get_object_or_404  #不使用render，改使用render_to_response
from .models import Blog,BlogType

def blog_list(request):
    context = {}
    context['blogs'] = Blog.objects.all()
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
