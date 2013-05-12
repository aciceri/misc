from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Article

def index(request):
	return HttpResponse('Pagina principale')

def article(request, article_id):
	a = Article.objects.get(id=article_id)
	context = {'article': a}
	return render(request, 'blog/article.html', context)

