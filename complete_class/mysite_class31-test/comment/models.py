from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import ContentType
# from django.contrib.auth.models import User
from django.conf import settings

class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id') 
    # content_object表示指向另一个model中的class的一个具体object

    text = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="comments", on_delete=models.CASCADE) # related_name表示反向解析的名字

    root = models.ForeignKey('self', related_name="root_comment", null=True, on_delete=models.CASCADE) # 这条回复的最顶级评论是什么
    parent = models.ForeignKey('self', related_name="parent_commment", null=True, on_delete=models.CASCADE) # 与自己形成外键关联，构成树结构
    reply_to = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="replies", null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.text   # 使admin中新增时能看到回复对象的内容

    class Meta:
        ordering = ['comment_time']