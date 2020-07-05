from django.contrib import admin
from .models import Article

# Register your models here.在这里注册你的模型
class ArticleAdmin(admin.ModelAdmin):
	list_display = ("title","content")  #元组或列表  最好元组

admin.site.register(Article,ArticleAdmin)