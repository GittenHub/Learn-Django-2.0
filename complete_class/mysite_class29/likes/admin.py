from django.contrib import admin
from .models import LikeCount, LikeRecord

@admin.register(LikeCount)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'liked_num')

@admin.register(LikeRecord)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'liked_time')