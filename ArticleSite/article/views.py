from django.shortcuts import render, get_object_or_404
from .models import ArticleType, Article

# Create your views here.
def article_list(request):
    article_types = ArticleType.objects.all()
    articles = Article.objects.all()
    context = {}
    context['article_types'] = article_types
    context['articles'] = articles
    return render(request, 'article_list.html', context)

def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    context = {}
    context['article'] = article
    return render(request, 'article_detail.html', context)

def article_with_type(request, article_type_pk):
    article_types = ArticleType.objects.all()
    article_type = get_object_or_404(ArticleType, pk=article_type_pk)
    articles = Article.objects.filter(article_type=article_type)
    context = {}
    context['article_type'] = article_type
    context['article_types'] = article_types
    context['articles'] = articles
    return render(request, 'article_with_type.html', context)

def article_with_date(request, article_pk):
    pass