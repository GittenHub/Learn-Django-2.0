# 课程基本信息
https://www.bilibili.com/video/BV1GW411Y7EU
**版本情况：**

# 环境配置
**官网文档：**
https://docs.djangoproject.com/zh-hans/2.1/
**下载Django：**
```
$ conda activate envs (envs) 
$ pip install Django==2.0
```
# 02 入门仪式：Hello World
## 创建项目命令：
```
$ django-admin startproject<项目名>
```
## Django项目基本结构
![ed612f399cb4e2100f43788d718f4b13.png](en-resource://database/3734:1)

## 响应请求
![7c0a63838c0410fa95561fbb1f0e0683.png](en-resource://database/3736:1)

## 根目录下创建views.py
```
#views.py  创建一个index方法
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, world")
```

## 在urls.py中新建一个路由
```
#urls.py 
from django.contrib import admin 
from django.urls import path 
from . import views 

urlpatterns = [     
    path('admin/', admin.site.urls),#后台管理网址     
    path('', views.index),   #设置一个空的路由，不设置就是ip后没有目录，需要创建一个方法 ]
```

## re_path与path的区别
是否使用正则表达式

## 启动本地服务
```
/mysite $ python manage.py runserver
```
## 迁移数据库
```
/mysite $ python manage.py migrate
```
数据库类型修改在settings.py中

## 默认后台管理
http://127.0.0.1:8000/admin

## 创建超级用户
```
$ python manage.py createsuperuser
```
账号：gitten
密码：guoyiteng

>命令行帮助：python manage.py help

# 03 基本响应结构
## 多种相似结构的页面处理方式
![febd9e0d984662b907e14b4d40c6e78f.png](en-resource://database/3738:1)
抽象处理为模型
## 创建一个应用
```
$ python manage.py startapp <应用名称>
```
编辑settings.py文件
```
#settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
  	...,
    'article'  
]
```
## 同步数据库
```
$ python manage.py makemigrations  #制造迁移
$ python manage.py migrate  #迁移
```
## 将app添加到网站的后台管理
编辑article这个app文件夹下的admin.py
## 将网站后台修改为中文
修改settings.py文件
```
#settings.py
...
LANGUAGE_CODE = 'zh-Hans'
```
## 查看文章页面
```
# article/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import Article  #引用创建的模型

# Create your views here.
def article_detail(request,article_id):
	return HttpResponse("文章id: %s" % article_id)
```
```
# urls.py
from django.contrib import admin
from django.urls import path
from . import views
from article.views import article_detail  #引用article包中views的article_detail方法

urlpatterns = [
   ...
    path('article/<int:article_id>', article_detail, name="article_detail"), #本行中的<int:article_id>代表这是一个整数变量，且变量名与对应views中的处理方法传递的参数相同;name是表示别名
]
```
## Objects
模型的objects是获取哦操作模型的对象
```
Article.objects.get(条件)
Article.objects.all()
Article.objects.filter(条件)
```