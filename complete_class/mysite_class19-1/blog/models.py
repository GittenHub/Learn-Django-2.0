from django.db import models
from django.db.models.fields import exceptions
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class BlogType(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name

class Blog(models.Model):
    title = models.CharField(max_length=50)
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING)
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)

    def get_read_num(self):
        try:
            return self.readnum.read_num   # 在将Blog和ReadNum关联后可以通过小写的方式调用另一个类的属性
        except exceptions.ObjectDoesNotExist as e: # 如果返回错误是对象不存在，则
            return 0
        

    def __str__(self):
        return "Blog: %s" % self.title

    class Meta:
        ordering = ['-created_time']  # 在最前面加负表示倒序，这里可以设置多个排序方式

class ReadNum(models.Model):
    read_num = models.IntegerField(default=0)
    blog = models.OneToOneField(Blog, on_delete=models.DO_NOTHING)  
    # OneToOneField表示一对一，ForeignKey表示多对一，ManyToManyField表示多对多;on_delete 删除阅读数时是否删除博客;
