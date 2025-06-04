from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.http import HttpResponse
from django.urls import reverse

from .forms import ArticleForm
from .models import Article


class ArticleListView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all().order_by("-created_at")
        return render(request, "articles/list.html", {"articles": articles})


class ArticleDetailView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs["id"])
        return render(request, "articles/detail.html", {"article": article})

# ----------------------------------------------------------------------------
class ArticleCreate(View):
    def get(self, request, *args, **kwargs):
        return redirect(reverse('article_list'))

def hello_view(request):
    return HttpResponse("Hello, Articles!")
