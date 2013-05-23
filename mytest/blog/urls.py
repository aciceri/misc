from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'blog.views.index', name='index'),
    url(r'^(?P<article_id>\d+)$', 'blog.views.article', name='article'),
    url(r'^all$', 'blog.views.all', name='all'),
    url(r'^search$', 'blog.views.search', name='search'),
)
