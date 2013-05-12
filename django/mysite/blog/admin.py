from django.contrib import admin
from blog.models import Article

class ArticleAdmin(admin.ModelAdmin):
	fields = ['title', 'content']
	list_display = ('title', 'datetime')

admin.site.register(Article, ArticleAdmin)
