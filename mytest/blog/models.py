from django.db import models
from django.contrib import admin
from markdown import markdown


class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    body_html = models.TextField(editable=True, blank=True, null=True)
    pub_date = models.DateTimeField()

    def save(self):
        self.body_html = markdown(self.body, ['tables'], output_format='html5')
        super(Article, self).save()


    def __str__(self):
        return self.title


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('', {'fields': ['title', 'pub_date']}),
        ('', {'fields': ['body', 'body_html']}),
    ]

    list_display = ('id', 'title', 'pub_date')


admin.site.register(Article, ArticleAdmin)
