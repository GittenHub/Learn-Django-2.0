from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ArticleType(models.Model):
    type_name = models.CharField(max_length=15)
    def __str__(self):
        return self.type_name

class Article(models.Model):
    title = models.CharField(max_length=50)
    article_type = models.ForeignKey(ArticleType, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_time']  # 在最前面加负表示倒序，这里可以设置多个排序方式