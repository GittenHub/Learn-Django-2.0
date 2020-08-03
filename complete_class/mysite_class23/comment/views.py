from django.shortcuts import render, redirect
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from .models import Comment


def update_comment(request):
    referer = request.META.get('HTTP_REFERER', reverse('home')) 
    # 转回到请求中的网址

    # 数据检查
    if not request.user.is_authenticated:
    # request.user.is_authenticated表示是否登录   
        return render(request, 'error.html', {'message':'用户未登录', 'redirect_to':referer})

    text = request.POST.get('text', '').strip()  # 获取不到为空
    if text == '':
        return render(request, 'error.html', {'message':'评论内容为空', 'redirect_to':referer})

    try:  # 进行错误处理，有可能content_type、object_id会有错误
        content_type = request.POST.get('content_type', '')
        object_id = int(request.POST.get('object_id', ''))
        model_class = ContentType.objects.get(model=content_type).model_class()
        # 使用ContentType进行处理，根据'content_type'得到blog等对象类型,ContentType.objects.get获得一个外键关联的具体的blog对象
        # 使用model_class方法，可以得到具体的模型的class, 也就是得到Blog；使用model_class方法，可以根据一个具体的object对象，返回这个对象所属的class类
        model_obj = model_class.objects.get(pk=object_id)
    except Exception as e:
        return render(request, 'error.html', {'message':'评论对象不存在', 'redirect_to':referer})

    # 检查通过，保存数据
    comment = Comment()
    comment.user = request.user
    comment.text = text
    comment.content_object = model_obj
    comment.save()

    return redirect(referer)