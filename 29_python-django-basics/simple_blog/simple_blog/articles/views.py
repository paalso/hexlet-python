from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from simple_blog.articles.models import Article
from simple_blog.categories.models import Category
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
        if form.is_valid():
            category_name = form.cleaned_data['category']
            category = Category.objects.get(name=category_name)
            article = Article(
                title=form.cleaned_data['title'],
                body=form.cleaned_data['body'],
                category=category
            )
            article.save()
            return redirect(reverse('articles_index'))

        return render(
            request,
            'articles/create.html',
            {'form': form}
        )
