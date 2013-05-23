from django.shortcuts import render
from blog.models import Article


def index(request):
    article = Article.objects.get(id=1)
    return render(request, 'blog/article.html', {'article': article})

def article(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'blog/article.html', {'article': article})

def all(request):
    articles = Article.objects.all()
    return render(request, 'blog/all.html', {'articles': articles})

def search(request):
    query = request.GET['q']
    articles = Article.objects.filter(body__contains=query)
    return render(request, 'blog/search.html', {'articles': articles, 'query': query})
