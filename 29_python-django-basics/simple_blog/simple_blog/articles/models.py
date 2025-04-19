from django.db import models


# BEGIN (write your solution here)
class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
# END
