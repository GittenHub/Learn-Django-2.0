from django.urls import path
from . import views

urlpatterns = [
	#localhost:8000/article/
    path('<int:article_id>', views.article_detail, name="article_detail"), #本行中的<int:article_id>代表这是一个整数变量，且变量名与对应views中的处理方法传递的参数相同;name是表示别名
    #localhost:8000/article/1
    path('', views.article_list, name="article_list"), 
]
