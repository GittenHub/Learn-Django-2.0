from django.shortcuts import render, redirect
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.http import JsonResponse
from .models import Comment
from .forms import CommentForm

def update_comment(request):
    referer = request.META.get('HTTP_REFERER', reverse('home'))
    comment_form = CommentForm(request.POST, user=request.user) # 进行实例化；使用python中的关键词传参数，传递user
    data = {}
    if comment_form.is_valid(): # 如果POST中的数据有效的话，就进行保存
        comment = Comment()
        comment.user = comment_form.cleaned_data['user']
        comment.text = comment_form.cleaned_data['text']
        comment.content_object = comment_form.cleaned_data['content_object']

        parent = comment_form.cleaned_data['parent']
        if parent:
            comment.root = parent.root if not parent.root is None else parent
            comment.parent = parent
            comment.reply_to = parent.user
        comment.save()

        # 返回数据
        data['status'] = 'SUCCESS'
        data['username'] = comment.user.get_nickname_or_username()
        #data['comment_time'] = comment.comment_time.strftime('%Y-%m-%d %H:%m:%S')
        data['comment_time'] = comment.comment_time.timestamp() # timestamp()是时间戳方法，返回一串数字
        data['text'] = comment.text
        data['content_type'] = ContentType.objects.get_for_model(comment).model
        data['reply_to'] = comment.reply_to.get_nickname_or_username() if not parent is None else ''
        data['pk'] = comment.pk 
        data['root_pk'] = comment.root.pk if not comment.root is None else ''
    else:
        data['status'] = 'ERROR'
        data['message'] = list(comment_form.errors.values())[0][0]  # 取错误信息中的values，并将其转为list，并取第一个
        #return render(request, 'error.html', {'message':comment_form.errors, 'redirect_to':referer})
    return JsonResponse(data)