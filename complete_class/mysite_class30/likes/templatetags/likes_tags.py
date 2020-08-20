from django import template
from django.contrib.contenttypes.models import ContentType
from ..models import LikeCount, LikeRecord

# 用于注册
register = template.Library()

# 注册为简单的模板标签
@register.simple_tag
def get_like_count(obj):
    content_type = ContentType.objects.get_for_model(obj)
    like_clount, created = LikeCount.objects.get_or_create(content_type=content_type, object_id=obj.pk)
    return like_clount.liked_num

@register.simple_tag(takes_context=True) # takes_context=True表示可以使用所在模板的模板变量
def get_like_status(context, obj):       # 这里的context表示blog/views.py中传递过去的context
    content_type = ContentType.objects.get_for_model(obj)
    user = context['user']   # context
    if not user.is_authenticated:
        return ''
    if LikeRecord.objects.filter(content_type=content_type, object_id=obj.pk, user=user).exists():
        return 'active'
    else:
        return ''

@register.simple_tag
def get_content_type(obj):
    content_type = ContentType.objects.get_for_model(obj)
    return content_type.model