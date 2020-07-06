from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=30) 
	content = models.TextField()  #用了两种字段模型来穿件类中的两个属性
	#created_time = models.DateTimeField() #设置日期，然后再admin.py中修改
	#created_time = models.DateTimeField(default=timezone.now)  #直接设置默认值为现在
	created_time = models.DateTimeField(auto_now_add = True)  #添加时使用当前时间
	last_updated_time = models.DateTimeField(auto_now = True) #自动用现在的时间给这个值

	def __str__(self):  #在这个类中添加一个方法  标注具体是什么对象
		return "<Article: %s>" % self.title