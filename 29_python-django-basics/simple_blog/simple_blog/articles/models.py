from django.db import models
from simple_blog.categories.models import Category


class Article(models.Model):
    title = models.CharField('title', max_length=255)
    body = models.CharField('body', max_length=255)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        """Represent model object."""
        return f'{self.title} ({self.category.name})'
