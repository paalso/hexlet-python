from django.http import Http404
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views import View
from .models import Article


# @csrf_exempt
class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(
            request,
            "articles/index.html",
            context={
                "articles": articles,
            },
        )

    def post(self, request, *args, **kwargs):
        article = {
            'title': request.POST['title'],
            'author': request.POST['author'],
        }
        Article.objects.create(**article)
        articles = Article.objects.all()[:15]
        return render(
            request,
            "articles/index.html",
            context={
                "articles": articles,
            },
        )


@require_http_methods(['GET'])
def articles_view(request, id):
    # BEGIN (write your solution here)
    article = Article.objects.get(id=id)
    if not article:
        raise Http404()
    # END
    return render(request, 'articles/article.html', context={'article': article})
