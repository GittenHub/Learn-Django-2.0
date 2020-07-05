from django.shortcuts import render,render_to_response,get_object_or_404 
#from django.http import HttpResponse,Http404
from .models import Article


# Create your views here.
# def article_detail(request,article_id):
# 	try:    #使用try  except  处理异常
# 		article = Article.objects.get(id=article_id)  # 创建一个名为article的对象
# 		context = {}
# 		context ['article_obj'] = article 
# 		#return render(request,"article_detail.html",context)#render有三个参数，request、HTML文件路径、传递的参数(字典形式)
# 		return render_to_response("article_detail.html",context)  #render_to_response只需要后面两个参数
# 	except Article.DoesNotExist:
# 		#return HttpResponse("不存在")
# 		raise Http404("not exist")
# 	#return HttpResponse("<h2>文章标题： %s </h2> <br>文章内容： %s " % (article.title,article.content)) 
# 	#使用article对象中的title属性

#使用get_object_or_404来处理异常
def article_detail(request,article_id):
	article = get_object_or_404(Article,pk=article_id) #两个参数，1、模型；2、条件主键
	context = {}
	context ['article_obj'] = article 
	return render_to_response("article_detail.html",context) 


def article_list(request):
	articles = Article.objects.all()
	context = {}
	context["articles"] = articles
	return render_to_response("article_list.html",context)
