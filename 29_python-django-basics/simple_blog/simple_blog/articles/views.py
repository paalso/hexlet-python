from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from django.views.decorators.http import require_http_methods


articles = [
    {'id': 1, 'title': '"How to foo?"', 'author': 'F. BarBaz'},
    {'id': 2, 'title': '"Force 101"', 'author': 'O-W. Kenobi'},
    {'id': 3, 'title': '"Top 10 skyscrapers"', 'author': 'K. Kong'},
    {'id': 4, 'title': '"Top 10 skyscrapers (jp. edition)"', 'author': 'K. Godzilla'},
    {'id': 5, 'title': '"5 min recepies"', 'author': 'H. Lector'},
]


@require_http_methods(['GET', 'POST'])
def index(request):
    if request.method == 'POST':
        article = {
            'id': int(request.POST['id']),
            'title': request.POST['title'],
            'author': request.POST['author']
        }
        articles.append(article)
    return render(request, 'articles/index.html', context={'articles': articles})


@require_http_methods(['GET'])
def articles_show(request, id):
    article = _find_article(id)
    if article:
        return render(request, 'articles/article.html', context={'article': article})
    if settings.DEBUG:
        return render(request, '404.html', status=404)
    raise Http404("Article not found")


def _find_article(id_):
    for article in articles:
        if article['id'] == id_:
            return  article
