from django.shortcuts import get_object_or_404, render
from django.views import View
from simple_blog.categories.models import Category

class IndexView(View):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        return render(request, 'categories/index.html', context={
            'categories': categories,
        })
