# Learn-Django-2.0
B站课程学习https://www.bilibili.com/video/BV1GW411Y7EU

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



# 08.常用的模版标签和过滤器

## 1、继续搭建blog

- [x] models 
- [x] admin
- [ ] views
- [ ] urls
- [ ] templates

在blog/models.py中新建两个类

在blog/views.py中新建两个方法

在blog文件夹下新建templates文件夹，再在templates中新建blog_list.html和blog_detail.html

在blog文件夹下新建urls.py文件，再在总urls.py文件中做好路由映射

## 2、常用的模板标签

- 循环： for
- 条件： if（可逻辑判断）、ifequal、ifnotequal
- 链接： url
- 模板嵌套：block、extends、include
- 注释：{# #}

### 标签

```html
 <h3>{{ blog.title }}</h3>   
{% url 'blog_detail' blog.pk %}
```

两种均为标签

## 3、常用的过滤器

- 日期：date
- 字数截取：truncatechars、truncatechars_html、truncatewords、truncatewords_html
- 是否信任html：safe
- 长度：length

> 参考：https://docs.djangoproject.com/zh-hans/2.0/ref/templates/builtins/

```html
<p>一共有{{ blogs|length }}篇博客</p>
<p>发表日期：{{ blog.created_time|date:"Y-m-d h:n:s" }}</p>
```

### 在templates中的html里使用过滤器

```html
<p>{{ blog.content|truncatechars:30 }}</p>   <!-- 过滤器，显示前30个字符 -->
<p>{{ blog.content|truncatewords:30 }}</p>   <!-- 过滤器，显示前30个英文单词，空格隔开 -->
```





# 09.模板嵌套

## 1、常用的模板标签

- 循环： for
- 条件： if（可逻辑判断）、ifequal、ifnotequal
- 链接： url
- 模板嵌套：block、extends、include
- 注释：{# #}

## 2、全局模板文件夹

在mysite总目录下心间templates文件夹

然后修改 settings.py -->TEMPLATES --> DIRS

```python
'DIRS': [
            os.path.join(BASE_DIR, 'templates'),    #定义全局模板文件夹路径
        ],
```



## 3、模板文件设置建议

- app模板文件 --> app
- project模板文件 --> project



# 10.使用CSS美化页面

## 1、页面设计

- 导航栏
- 主题内容
- 尾注

### 导航栏设计

LOGO网站名称 + 导航

xxxxx的网站   首页  博客

## 2、使用CSS

CSS ：层叠样式表   修饰HTML

韩顺平老师  学习html+css   w3cschool

##  3、使用静态文件

CSS代码  -->  CSS文件（js文件、图片）  统称为静态文件

设置静态文件的路径，在settings.py最后增加

```python
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),   #设置静态文件的路径
]
```



### 方法一：直接在HTML模板中引入css

```html
<link rel="stylesheet" type="text/css" href="/static/base.css">
```

### 方法二：load staticfiles

在模板文件中

```html
{% load staticfiles %}

<link rel="stylesheet" type="text/css" href="{% static 'base.css' %}">
{% block header_extends %}{% endblock %}
```

```html
{% load staticfiles %}

{% block header_extends %}
    <link rel="stylesheet" type="text/css" href="{% static 'home.css'%}">
{% endblock %}
```



# 11.CSS框架协助前段布局

## 1、为什么用CSS框架

1. 不会或不怎么会CSS
2. 不知道如何设计前段样式
3. 从头到尾写整个网站的CSS代码量大
4. ...

##  2、如何选择CSS框架

- 易用性
- 兼容性
- 大小
- 效果
- 功能

### bootstrap

- 文档齐全，使用简单
- 兼容较多浏览器
- 非轻量级
- 扁平、简洁
- 组件齐全、响应式

## 3、部署Bootstrap

1. 打开bootstrap[www.bootcss.com](www.bootcss.com)
2. 下载bootstrap（选择用于生产环境的bootstrap）
3. 引用bootstrap
4. 开始使用

### bootstrap基本模板

1. 中文语言设置

   ```HTML
   <html lang="zh-CN">
   ```

2. 头信息设置

   ```html
   <meta charset="utf-8">
   <meta http-equiv="X-UA-Compatible" content="IE=edge">  
   <!-- 告诉ie浏览器使用什么内核 -->
   <meta name="viewport" content="width=device-width, initial-scale=1">
   <!-- 响应式布局 -->
   ```

   

# 12.Bootstrap响应式布局

> 同时打开两个Django项目的runserver
>
> `python manage.py runserver 8001  #默认为8080端口，设置其他端口则直接加在最后`

## 1、Bootstrap的响应式设计

适应4种屏幕大小，12列布局

- <768px （手机）
- \>=768px （平板）
- \>=992px （小尺寸显示器）
- \>=1200px （大尺寸显示器）

### 栅格参数

通过下表可以详细查看 Bootstrap 的栅格系统是如何在多种屏幕设备上工作的。

|                       | 超小屏幕 手机 (<768px)     | 小屏幕 平板 (≥768px)                                | 中等屏幕 桌面显示器 (≥992px) | 大屏幕 大桌面显示器 (≥1200px) |
| :-------------------- | :------------------------- | :-------------------------------------------------- | :--------------------------- | :---------------------------: |
| 栅格系统行为          | 总是水平排列               | 开始是堆叠在一起的，当大于这些阈值时将变为水平排列C |                              |                               |
| `.container` 最大宽度 | None （自动）              | 750px                                               | 970px                        |            1170px             |
| 类前缀                | `.col-xs-`                 | `.col-sm-`                                          | `.col-md-`                   |          `.col-lg-`           |
| 列（column）数        | 12                         |                                                     |                              |                               |
| 最大列（column）宽    | 自动                       | ~62px                                               | ~81px                        |             ~97px             |
| 槽（gutter）宽        | 30px （每列左右均有 15px） |                                                     |                              |                               |
| 可嵌套                | 是                         |                                                     |                              |                               |
| 偏移（Offsets）       | 是                         |                                                     |                              |                               |
| 列排序                | 是                         |                                                     |                              |                               |

### 布局容器

Bootstrap 需要为页面内容和栅格系统包裹一个 `.container` 容器。我们提供了两个作此用处的类。注意，由于 `padding` 等属性的原因，这两种 容器类不能互相嵌套。

`.container` 类用于固定宽度并支持响应式布局的容器。

```
<div class="container">
  ...
</div>
```

`.container-fluid` 类用于 100% 宽度，占据全部视口（viewport）的容器。

```
<div class="container-fluid">
  ...
</div>
```



## 2、基本结构

```html
<div class="container">
  	<div class="row">
	      <div class="col-xx-*"></div>
      	<div class="col-xx-*"></div>
	  </div>
</div>
```





## 3、Django静态文件命名空间

为了避免冲突

可以在app文件夹下的static文件夹中心间app名称的文件夹，再将css等静态文件放入其中，在应用css前加`static/app/xxx.css`



# 13.分页和shell命令行模式

## 1、为什么先将分页功能

1. 新增或编辑博客内容

2. 博客文章数较多->全部加载过慢->分页加载

   为了夯实基础，借机讲shell模式、模型操作、模版标签、分页器

## 2、快速添加博客

### shell命令行模式添加博客

1. `python manage.py shell`
2. `for`循环执行新增博客代码

## 3、模型新增对象

```python
from blog.models import Blog
blog = Blog()
blog.title = 'xxx'
...
blog.save()
```

### terminal操作

```python
Last login: Mon Jul 13 14:12:14 on ttys000
gitten@Gittens-Macbook mysite % conda activate django2.0
(django2.0) gitten@Gittens-Macbook mysite % python manage.py shell
Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
[Clang 10.0.0 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from blog.models import Blog
>>> dir()
['Blog', '__builtins__']
>>> Blog.objects.all()
<QuerySet [<Blog: Blog: 长内容的博客>, <Blog: Blog: 随笔2>, <Blog: Blog: Django1>]>
>>> Blog.objects.count()
3
>>> Blog.objects.all().count()
3
>>> blog = Blog()
>>> dir()
['Blog', '__builtins__', 'blog']
>>> Blog.objects.all()
<QuerySet [<Blog: Blog: 长内容的博客>, <Blog: Blog: 随笔2>, <Blog: Blog: Django1>]>
>>> blog.title = "shell下第1篇"
>>> blog.content = "xxxxxx"
>>> from blog.models import BlogType
>>> BlogType.objects.all()
<QuerySet [<BlogType: Django>, <BlogType: 随笔>, <BlogType: 感悟>]>
>>> BlogType.objects.all()[0]
<BlogType: Django>
>>> blog_type = BlogType.objects.all()[0]
>>> blog.blog_type = blog_type
>>> from django.contrib.auth.models import User
>>> User.objects.all()
<QuerySet [<User: gitten>]>
>>> user = User.objects.all()[0]
>>> blog.author = user
>>> blog.save()
>>> Blog.objects.all()
<QuerySet [<Blog: Blog: 长内容的博客>, <Blog: Blog: 随笔2>, <Blog: Blog: Django1>, <Blog: Blog: shell下第1篇>]>
>>>
>>>
>>>
>>>
>>> for i in range(1,31):
...     blog = Blog()
...     blog.title = "for %s" %i
...     blog.content = "xxxxx:%s" % i
...     blog.blog_type = blog_type
...     blog.author = user
...     blog.save()
... 
>>> Blog.objects.all().count()
34
```

## 4、分页器实现分页

![](https://gitee.com/gitten/PicBed/raw/master/20200714102155.png)



```python
(django2.0) gitten@Gittens-Macbook mysite % python manage.py shell
Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
[Clang 10.0.0 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> dir()
['__builtins__']
>>> from django.core.paginator import Paginator
>>> from blog.models import Blog
>>> blogs = Blog.object.all()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: type object 'Blog' has no attribute 'object'
>>> blogs = Blog.objects.all()
>>> blogs.count()
34
>>> paginator = Paginator(blogs,10)
<console>:1: UnorderedObjectListWarning: Pagination may yield inconsistent results with an unordered object_list: <class 'blog.models.Blog'> QuerySet.
# 这里报了一个错误，是因为我们在models中没有设置默认排序方式，去修改
>>> 
```

### 修改models.py的默认排序方式

## 5、分页的使用

前端：发送请求，请求打开具体分页内容

后端：处理情况，返回具体分页内容相应情况

` http://127.0.0.1:8000/blog/?page=4`中的`?page=4`表示GET传递的参数





# 14. 优化分页展示

## 1、优化页面展示

友好的用户体验

1. 当前页面高亮
2. 不好过多页码选择，影响布局









