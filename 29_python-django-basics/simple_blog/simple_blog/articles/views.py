from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from simple_blog.articles.models import Article
from django.urls import reverse
from simple_blog.articles.forms import ArticleForm


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        return render(
            request,
            'articles/index.html',
            context={
            'articles': articles,
        }
    )


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(
            request,
            'articles/article.html',
            context={
            'article': article,
        }
    )


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
        if form.is_valid():  # Если данные корректные, то сохраняем данные формы
            form.save()
            return redirect(reverse('articles_index'))  # Редирект на указанный маршрут
        # Если данные некорректные, то возвращаем человека обратно на страницу с заполненной формой
        return render(request, 'articles/create.html', {'form': form})


class ArticleFormEditView(View):
    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(
            request, 'articles/update.html', {'form': form, 'article_id': article_id}
        )

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect(reverse('articles_index'))
    
        return render(
            request, 'articles/update.html', {'form': form, 'article_id': article_id}
        )
