from django.db import models

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=30) 
	content = models.TextField()  #用了两种字段模型来穿件类中的两个属性

	def __str__(self):  #在这个类中添加一个方法  标注具体是什么对象
		return "<Article: %s>" % self.title