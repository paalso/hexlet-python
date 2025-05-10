from .models import Article
from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField(label='Заголовок', max_length=255)
    body = forms.CharField(label='Содержание', max_length=255)
    category = forms.CharField(label='Категория', max_length=255)
