<a name="index">**目录**</a><br><a href="#0">课程基本信息</a>  
<a href="#1">环境配置</a>  
<a href="#2">02 入门仪式：Hello World</a>  
&emsp;<a href="#3">创建项目命令：</a>  
&emsp;<a href="#4">Django项目基本结构</a>  
&emsp;<a href="#5">响应请求</a>  
&emsp;<a href="#6">根目录下创建views.py</a>  
&emsp;<a href="#7">在urls.py中新建一个路由</a>  
&emsp;<a href="#8">re_path与path的区别</a>  
&emsp;<a href="#9">启动本地服务</a>  
&emsp;<a href="#10">迁移数据库</a>  
&emsp;<a href="#11">默认后台管理</a>  
&emsp;<a href="#12">创建超级用户</a>  
<a href="#13">03 基本响应结构</a>  
&emsp;<a href="#14">多种相似结构的页面处理方式</a>  
&emsp;<a href="#15">创建一个应用</a>  
&emsp;<a href="#16">同步数据库</a>  
&emsp;<a href="#17">将app添加到网站的后台管理</a>  
&emsp;<a href="#18">将网站后台修改为中文</a>  
<a href="#19">04.使用模版显示内容</a>  
&emsp;<a href="#20">查看文章页面</a>  
<a href="#21">article/views.py</a>  
<a href="#22">Create your views here.</a>  
<a href="#23">urls.py</a>  
&emsp;<a href="#24">Objects</a>  
&emsp;&emsp;<a href="#25">objects.get()</a>  
<a href="#26">Create your views here.</a>  
&emsp;&emsp;&emsp;<a href="#27">.get()方法错误异常处理</a>  
<a href="#28">Create your views here.</a>  
&emsp;<a href="#29">使用模板</a>  
&emsp;<a href="#30">获取文章列表</a>  
&emsp;<a href="#31">总urls包含app的urls</a>  
<a href="#32">article/urls.py</a>  
<a href="#33">修改总路由urls.py文件的内筒，使用include</a>  
<a href="#34">05.定制后台和修改模型</a>  

# <a name="0">课程基本信息</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>

https://www.bilibili.com/video/BV1GW411Y7EU
**版本情况：**

# <a name="1">环境配置</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
**官网文档：**
https://docs.djangoproject.com/zh-hans/2.1/
**下载Django：**

```
$ conda activate envs (envs) 
$ pip install Django==2.0
```
# <a name="2">02 入门仪式：Hello World</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
## <a name="3">创建项目命令：</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
$ django-admin startproject<项目名>
```
## <a name="4">Django项目基本结构</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
![](https://raw.githubusercontent.com/GittenHub/GittenPicRepo/master/Image.png)

## <a name="5">响应请求</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
![](https://raw.githubusercontent.com/GittenHub/GittenPicRepo/master/Imag1e.png)

## <a name="6">根目录下创建views.py</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```python
#views.py  创建一个index方法
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, world")
```

## <a name="7">在urls.py中新建一个路由</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```python
#urls.py 
from django.contrib import admin 
from django.urls import path 
from . import views 

urlpatterns = [     
    path('admin/', admin.site.urls),#后台管理网址     
    path('', views.index),   #设置一个空的路由，不设置就是ip后没有目录，需要创建一个方法 ]
```

## <a name="8">re_path与path的区别</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
是否使用正则表达式

## <a name="9">启动本地服务</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
/mysite $ python manage.py runserver
```
## <a name="10">迁移数据库</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
/mysite $ python manage.py migrate
```
数据库类型修改在settings.py中

## <a name="11">默认后台管理</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
http://127.0.0.1:8000/admin

## <a name="12">创建超级用户</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
$ python manage.py createsuperuser
```
账号：gitten
密码：guoyiteng

>命令行帮助：python manage.py help

# <a name="13">03 基本响应结构</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
## <a name="14">多种相似结构的页面处理方式</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
![](https://raw.githubusercontent.com/GittenHub/GittenPicRepo/master/Image2.png)
抽象处理为模型

## <a name="15">创建一个应用</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
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
## <a name="16">同步数据库</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
$ python manage.py makemigrations  #制造迁移
$ python manage.py migrate  #迁移
```
## <a name="17">将app添加到网站的后台管理</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
编辑article这个app文件夹下的admin.py
## <a name="18">将网站后台修改为中文</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
修改settings.py文件
```python
#settings.py
...
LANGUAGE_CODE = 'zh-Hans'
```


# <a name="19">04.使用模版显示内容</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>

## <a name="20">查看文章页面</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>

```python
# <a name="21">article/views.py</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
from django.shortcuts import render
from django.http import HttpResponse
from .models import Article  #引用创建的模型

# <a name="22">Create your views here.</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
def article_detail(request,article_id):
	return HttpResponse("文章id: %s" % article_id)
```
```python
# <a name="23">urls.py</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
from django.contrib import admin
from django.urls import path
from . import views
from article.views import article_detail  #引用article包中views的article_detail方法

urlpatterns = [
   ...
    path('article/<int:article_id>', article_detail, name="article_detail"), #本行中的<int:article_id>代表这是一个整数变量，且变量名与对应views中的处理方法传递的参数相同;name是表示别名
]
```
## <a name="24">Objects</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
模型的objects是获取哦操作模型的对象
```python
Article.objects.get(条件)
Article.objects.all()
Article.objects.filter(条件)
```

### <a name="25">objects.get()</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>

```python
from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

# <a name="26">Create your views here.</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
def article_detail(request,article_id):
	article = Article.objects.get(id=article_id)  # 创建一个名为article的对象
	return HttpResponse("<h2>文章标题： %s </h2> <br>文章内容： %s " % (article.title,article.content)) 
	#使用article对象中的title属性
```

#### <a name="27">.get()方法错误异常处理</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>

try、except

```
from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Article

# <a name="28">Create your views here.</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
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



## <a name="29">使用模板</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>

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



## <a name="30">获取文章列表</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>

1. 在urls.py中配置路径

2. 在views.py中新建方法

3. 在HTML模板中使用for语句和url标签

   ```html
   {% for article in articles %}  <!-- 模板中的for语句 -->
   <!-- <a href="/article/{{article.pk}}">{{article.title}}</a> -->
   <a href="{% url 'article_detail' article.pk %}">{{article.title}}</a>   <!-- 模板中的URL标签 -->
   {% endfor %}
   ```



## <a name="31">总urls包含app的urls</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>

1. 在“article”APP中新建APP的urls.py文件
2. 在总路由urls.py文件中使用include将article中的urls引用过来

```python
# <a name="32">article/urls.py</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
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
# <a name="33">修改总路由urls.py文件的内筒，使用include</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
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



# <a name="34">05.定制后台和修改模型</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>

https://www.bilibili.com/video/BV1LW411877A/

















