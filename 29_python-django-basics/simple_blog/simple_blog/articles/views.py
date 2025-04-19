from django.http import Http404
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .models import Article


# @csrf_exempt
@require_http_methods(['GET', 'POST'])
def index(request):
    # BEGIN (write your solution here)
    if request.method == 'POST':
        article = {
            'title': request.POST['title'],
            'author': request.POST['author']
        }
        Article.objects.create(**article)
    articles = Article.objects.all()
    # END
    return render(request, 'articles/index.html', context={'articles': articles})


@require_http_methods(['GET'])
def article_view(request, id):
    # BEGIN (write your solution here)
    article = Article.objects.get(id=id)
    if not article:
        raise Http404()
    # END
    return render(request, 'articles/article.html', context={'article': article})
