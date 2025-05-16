# simple_journal/articles/views.py

import logging
from django.views import View
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from simple_journal.articles.models import Article
from simple_journal.articles.forms import ArticleForm
from django.views.decorators.csrf import csrf_exempt

logger = logging.getLogger(__name__)


class ArticleFormView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(
            request,
            'articles/create.html',
            {'form': form}
        )

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)

        # self._print_log_info('\nrequest.POST:', request.POST)
        logger.debug('\nrequest.POST: %s\n', request.POST)

        if form.is_valid():
            article = form.save()  # <- Всё делается здесь: и title, и content, и category
            logger.info('\nArticle created: %s\n', article)
            return redirect(reverse('articles_index'))

        return render(
            request,
            'articles/create.html',
            {'form': form}
        )

    @staticmethod
    def _print_log_info(header, info):
        print(header)
        print(info)
        print()
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
