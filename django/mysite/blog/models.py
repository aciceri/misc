from django.db import models

class Article(models.Model):
	title = models.CharField(max_length=100, unique=True)
	content = models.TextField()
	datetime = models.DateTimeField(db_index=True, auto_now_add=True)
	
	def __str__(self):
		return self.title
