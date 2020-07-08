from django.db import models
#from django.utils import timezone
from django.contrib.auth.models import User   #引入用户包


# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=30) 
	content = models.TextField()  #用了两种字段模型来穿件类中的两个属性
	#created_time = models.DateTimeField() #设置日期，然后再admin.py中修改
	#created_time = models.DateTimeField(default=timezone.now)  #直接设置默认值为现在
	created_time = models.DateTimeField(auto_now_add = True)  #添加时使用当前时间，只有在新增的时候数值会变
	last_updated_time = models.DateTimeField(auto_now = True) #自动用现在的时间给这个值，每次修改后数值都会改变
	author = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)  
	#几个参数：1、关联到哪个表；2、文章删除时是否删除作者；3、默认值，在这作者对应的外键的值
	is_deleted = models.BooleanField(default=False)  #逻辑删除，而不是真实在数据库中删除
	readed_num = models.IntegerField(default=0)  #阅读量

	def __str__(self):  #在这个类中添加一个方法  标注具体是什么对象
		return "<Article: %s>" % self.title