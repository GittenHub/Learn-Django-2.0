from django.contrib import admin
from .models import BlogType, Blog #, ReadNum
# Register your models here.

@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id','type_name')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'blog_type', 'author', 'get_read_num', 'created_time', 'last_updated_time') 
    # readnum表示models.py中创建的ReadNum类的小写
    # list_display中的是字段，只能是models中属性或方法
    # 此刻的get_read_num表示的是models中Blog类里的get_read_num方法
