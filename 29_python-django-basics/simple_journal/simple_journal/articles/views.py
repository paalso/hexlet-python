from django.views import View
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from simple_journal.articles.models import Article
# from simple_journal.articles.forms import ArticleForm


# BEGIN (write your solution here)

# END


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/article.html', context={
            'article': article,
        })
