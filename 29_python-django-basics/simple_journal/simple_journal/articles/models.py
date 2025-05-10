from django.db import models
from django.utils import timezone
from simple_journal.categories.models import Category


class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
