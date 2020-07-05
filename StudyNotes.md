# 目录

[TOC]

----------











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
![](https://raw.githubusercontent.com/GittenHub/GittenPicRepo/master/Image.png)

## 响应请求
![](https://raw.githubusercontent.com/GittenHub/GittenPicRepo/master/Imag1e.png)

## 根目录下创建views.py
```python
#views.py  创建一个index方法
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, world")
```

## 在urls.py中新建一个路由
```python
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
![](https://raw.githubusercontent.com/GittenHub/GittenPicRepo/master/Image2.png)
抽象处理为模型

## 创建一个应用
```
$ python manage.py startapp <应用名称>
```
编辑settings.py文件
```python
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
```python
#settings.py
...
LANGUAGE_CODE = 'zh-Hans'
```


# 04.使用模版显示内容

## 查看文章页面

```python
# article/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import Article  #引用创建的模型

# Create your views here.
def article_detail(request,article_id):
	return HttpResponse("文章id: %s" % article_id)
```
```python
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
```python
Article.objects.get(条件)
Article.objects.all()
Article.objects.filter(条件)
```

### objects.get()

```python
from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

# Create your views here.
def article_detail(request,article_id):
	article = Article.objects.get(id=article_id)  # 创建一个名为article的对象
	return HttpResponse("<h2>文章标题： %s </h2> <br>文章内容： %s " % (article.title,article.content)) 
	#使用article对象中的title属性
```

#### .get()方法错误异常处理

try、except

```
from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Article

# Create your views here.
def article_detail(request,article_id):
	try:    #使用try  except  处理异常
		article = Article.objects.get(id=article_id)  # 创建一个名为article的对象
	except Article.DoesNotExist:
		#return HttpResponse("不存在")
		raise Http404("not exist")
	return HttpResponse("<h2>文章标题： %s </h2> <br>文章内容： %s " % (article.title,article.content)) 
	#使用article对象中的title属性
```

get_object_or_404处理异常

```python
from django.shortcuts import render,render_to_response,get_object_or_404 
from .models import Article

def article_detail(request,article_id):
		article = get_object_or_404(Article,pk=article_id) #两个参数，1、模型；2、条件主键
		context = {}
		context ['article_obj'] = article 
		return render_to_response("article_detail.html",context) 
```



## 使用模板

1. 在mysite/article下新建文件夹<templates>

2. 在templates文件中新建HTML文件“article_detail.html"

   ```
   <!DOCTYPE html>
   <html>
   <head>
   	<title></title>
   </head>
   <body>
   	<h2>{{article_obj.title}}</h2>
   	<hr>
   	<p>{{article_obj.content}}</p>
   </body>
   </html>
   ```

   其中`{{}}`中的内容用于传递参数

> 查找翻看Django源代码，在Python的安装路径下/Lib/site-packages/django/包名



## 获取文章列表

1. 在urls.py中配置路径

2. 在views.py中新建方法

3. 在HTML模板中使用for语句和url标签

   ```html
   {% for article in articles %}  <!-- 模板中的for语句 -->
   <!-- <a href="/article/{{article.pk}}">{{article.title}}</a> -->
   <a href="{% url 'article_detail' article.pk %}">{{article.title}}</a>   <!-- 模板中的URL标签 -->
   {% endfor %}
   ```



## 总urls包含app的urls

1. 在“article”APP中新建APP的urls.py文件
2. 在总路由urls.py文件中使用include将article中的urls引用过来

```python
# article/urls.py
from django.urls import path
from . import views

urlpatterns = [
	#localhost:8000/article/
    path('<int:article_id>', views.article_detail, name="article_detail"), #本行中的<int:article_id>代表这是一个整数变量，且变量名与对应views中的处理方法传递的参数相同;name是表示别名
    #localhost:8000/article/1
    path('', views.article_list, name="article_list"), 
]
```

```python
# 修改总路由urls.py文件的内筒，使用include
from django.contrib import admin
from django.urls import path,include
from . import views
from article.views import article_detail,article_list

urlpatterns = [
    path('admin/', admin.site.urls),#后台管理网址
    path('', views.index),   #设置一个空的路由，不设置就是ip后没有目录，需要创建一个方法
    path('article/', include('article.urls')), #使用include引用app中的urls.py
]
```



# 05.定制后台和修改模型

https://www.bilibili.com/video/BV1LW411877A/

## 定制admin后台

设置模型\__str__

### 修改article/modles.py

```python
from django.db import models
# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=30) 
	content = models.TextField()  #用了两种字段模型来穿件类中的两个属性

	def __str__(self):  #在这个类中添加一个方法  标注具体是什么对象
		return "<Article: %s>" % self.title
```

### 修改article/admin.py

```python
from django.contrib import admin
from .models import Article

# Register your models here.在这里注册你的模型
class ArticleAdmin(admin.ModelAdmin):
	list_display = ("title","content")  #元组或列表  最好元组

admin.site.register(Article,ArticleAdmin)
```

修改前的admin界面：

![](https://raw.githubusercontent.com/GittenHub/GittenPicRepo/master/20200705233931.png)

修改后：

![image-20200705234038390](C:\Users\Gitten\AppData\Roaming\Typora\typora-user-images\image-20200705234038390.png)











