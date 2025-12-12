from django.db import models
from django.contrib.auth.models import User


class NewsArticle(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    content = models.TextField(verbose_name='Content')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Author',
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Date of last update')
    is_published = models.BooleanField(verbose_name='Is published')
    
    def __str__(self):
        return self.title
    