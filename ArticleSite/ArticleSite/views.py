from django.shortcuts import render, get_object_or_404
from article.models import ArticleType, Article

# Create your views here.
def home(request):
    articles = Article.objects.all()
    article_types = ArticleType.objects.all()
    context = {}
    context['articles'] = articles
    context['article_types'] = article_types
    context['articles_t1'] = Article.objects.filter(article_type=get_object_or_404(ArticleType, pk=1))[0:10]
    context['articles_t2'] = Article.objects.filter(article_type=get_object_or_404(ArticleType, pk=2))[0:10]

    return render(request, 'home.html', context)
