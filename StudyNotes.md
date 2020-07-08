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

![](https://raw.githubusercontent.com/GittenHub/GittenPicRepo/master/20200706133259.png)

### 修改id排序（降序、升序）：

#### 在admin.py中修改

```python
class ArticleAdmin(admin.ModelAdmin):
	list_display = ("id","title","content")  #元组或列表  最好元组
	ordering = ("id",)  #注意在这要加一个逗号，代表是一个元组，否则识别为普通括号
  #ordering = ("-id",)  #倒序
```

#### 在models.py中修改



## 修改模型

> 修改模型后需要生成迁移文件，再迁移
>
> ` python manage.py makemigrations`
>
> ` python manage.py migrate`

> 修改模型前备份数据库

### 让文章显示创建日期的三种方法（设置默认值）

1. 修改models.py，在Article类中增加属性`created_time = models.DateTimeField()`，然后在admin.py中的ArticleAdmin中的list_display属性元组中增加"created_time"字段，迁移启动服务器后，在终端中设置：选择1，输入timezone.now
2. 修改admin.py直接在Article类中增加属性`created_time = models.DateTimeField(default=timezone.now)`设置默认值为现在的日期（记得import）
3. 在`models.DateTimeField(auto_now_add = True) `使用默认参数`auto_now_add = True`



### 外间 作者的名称

Django自带用户模型，在模型中的Article类中新增author属性，用models.ForeignKey()关联外键到User库

```python
#article/models.py/Article
from django.contrib.auth.models import User   #引入用户包

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1) 
	#几个参数：1、关联到哪个表；2、文章删除时是否删除作者；3、默认值，在这作者对应的外键的值

```

再在admin.py中增加"author"

### 文章逻辑删除

```python
#article/models.py/Article
from django.db import models

class Article(models.Model):
    is_deleted = models.BooleanField(default=False)  #逻辑删除，而不是真实在数据库中删除
	readed_num = models.IntegerField(default=0)  #阅读量
```

再在admin.py中增加"is_deleted"、""

文章列表（http://127.0.0.1:8000/article/）中不显示逻辑删除的文章：

```python
#article/views.py
def article_list(request):
	articles = Article.objects.filter(is_deleted = False)  #只筛选出未逻辑删除的文章
```





# 06.开始完整制作网站

动力影响学习的热情



## 如何用Django开发网站

要做什么

设计网站圆形

具体开发

测试

部署上线



业务流程

功能木块

前端布局

后端模型



## 接下来的教程

### 目的

1. 通过完整的开发过程学习Django
2. 对一般的网站开发有全面的认识

### 个人博客网站

- 项目管理
  - IDE
  - 本地虚拟环境
  - Git/Github

- 前端开发
  - HTML + JavaScript + CSS
  - jQuery
  - Bootstrap
  - ajax
- 后端开放
  - 博客管理和展示
  - 用户登录和注册
  - 评论和回复
  - 点赞
- 数据库和服务器
  - MySQL
  - linux（centos、Ubuntu）
  - 网站部署

### IDE

记事本

vim/Emacs

sublime text

PyCharm



# 07.构建个人博客网站

## 1.简单构建

网站的功能模块：

- 博客
  - 博文
  - 博客分类
  - 博客标签
- 评论
  - 
- 点赞
- 阅读
- 用户-->第三方登录（QQ/微博）

> 功能模块 ≈ Django App



## 2.开启本地虚拟环境

隔开python项目的运行环境

1. 避免多个项目之间python库的冲突
2. 完整便捷到处python库的列表

`$ pip install virtualenv`

## 3.virtualenv的使用方法

- 创建：`virtualenv<虚拟环境名称>`
- 启动：`$ cd 虚拟环境名称\Scripts\activate`  
- 退出：`deactivate`

## 4.初步创建blog应用

博文 + 博客分类

- 一篇博客一种分类，本教程采用这种
- 一篇博客多种分类

```
django-admin startproject mysite
python manage.py startapp blog
python manage.py migrate
python manage.py createsuperuser
```

> 用户名：gitten
>
> 密码：guoyiteng



## 5.pip一键到处和安装（拓展）

`pip freeze > requirements.txt`

`pip install -r requirements.txt`





































