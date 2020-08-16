from django import template
from django.contrib.contenttypes.models import ContentType
from ..models import Comment
from ..forms import CommentForm

# 用于注册
register = template.Library()

# 注册为简单的模板标签
@register.simple_tag
def get_comment_count(obj):
    content_type = ContentType.objects.get_for_model(obj)
    return Comment.objects.filter(content_type=content_type, object_id=obj.pk).count()

@register.simple_tag    
def get_comment_form(obj):
    content_type = ContentType.objects.get_for_model(obj)
    form = CommentForm(initial={
        'content_type':content_type.model, 
        'object_id':obj.pk, 
        'reply_comment_id': 0}) 
    # 对forms表单中的类进行初始化定义值，方便前端代码调用，initial对应的是一个list; blog_content_type是一个对象，blog_content_type.model是这个对象名称字符串
    return form

@register.simple_tag
def get_comment_list(obj):
    content_type = ContentType.objects.get_for_model(obj)
    comments = Comment.objects.filter(content_type=content_type, object_id=obj.pk, parent=None) # parent=None表示只显示一级评论
    return comments.order_by('-comment_time')