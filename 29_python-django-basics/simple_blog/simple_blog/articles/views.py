from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse
import json

articles = [
    {'title': '"How to foo?"', 'author': 'F. BarBaz'},
    {'title': '"Force 101"', 'author': 'O-W. Kenobi'},
    {'title': '"Top 10 skyscrapers"', 'author': 'K. Kong'},
    {'title': '"Top 10 skyscrapers (jp. edition)"', 'author': 'K. Godzilla'},
    {'title': '"5 min recepies"', 'author': 'H. Lector'},
]


@csrf_exempt
@require_http_methods(["GET", "POST"])
def index(request):
    if request.method == "POST":
        title = request.POST['title']
        author = request.POST['author']
        quoted_title = f'"{title}"'
        articles.append({'title': quoted_title, 'author': author})
        print(articles)
    return render(
        request,
        template_name='articles.html',
        context={
            'articles': articles
        }
    )
