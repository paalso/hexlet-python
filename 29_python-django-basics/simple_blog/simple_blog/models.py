from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField()


class Employee(models.Model):
    POSITION_CHOICES = [
        ('TR', 'Trainee'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('CEO', 'CEO')
    ]
    name = models.CharField(max_length=255)
    position = models.CharField(
        max_length=3,
        choices=POSITION_CHOICES,
        default='TR',
    )
