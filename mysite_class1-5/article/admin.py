from django.contrib import admin
from .models import Article

# Register your models here.在这里注册你的模型
@admin.register(Article)  #修饰器，与admin.site.register(Article,ArticleAdmin)效果相同
class ArticleAdmin(admin.ModelAdmin):
	list_display = ("id","title","content","author","is_deleted","created_time","last_updated_time")  #元组或列表  最好元组
	ordering = ("id",)  #注意在这要加一个逗号，代表是一个元组，否则识别为普通括号
	#ordering = ("-id",)  #倒序

#admin.site.register(Article,ArticleAdmin)