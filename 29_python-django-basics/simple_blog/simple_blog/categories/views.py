from django.shortcuts import get_object_or_404, render
from django.views import View
from simple_blog.categories.models import Category


class IndexView(View):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        return render(request, 'categories/index.html', context={
            'categories': categories,
        })


class CategoryView(View):
    def get(self, request, *args, **kwargs):
        category = get_object_or_404(Category, id=kwargs['id'])
        category_articles = category.article_set.all()
        return render(
            request,
            'categories/category.html',
            context={
            'category': category,
            'category_articles': category_articles
        }
    )
