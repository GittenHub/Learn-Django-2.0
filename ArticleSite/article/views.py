from django.shortcuts import render, get_object_or_404
from .models import ArticleType, Article

# Create your views here.
def article_types_list(request):
    article_types = ArticleType.objects.all()
    context = {}
    context['article_types'] = article_types
    return render(request, 'article_types_list.html', context)

def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    context = {}
    context['article'] = article
    return render(request, 'article_detail.html', context)

def article_with_type(request, article_pk):
    pass

def article_with_date(request, article_pk):
    pass