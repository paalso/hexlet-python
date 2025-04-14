from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views import View

from django.http import HttpResponse

articles = [
    {'title': '"How to foo?"', 'author': 'F. BarBaz'},
    {'title': '"Force 101"', 'author': 'O-W. Kenobi'},
    {'title': '"Top 10 skyscrapers"', 'author': 'K. Kong'},
    {'title': '"Top 10 skyscrapers (jp. edition)"', 'author': 'K. Godzilla'},
    {'title': '"5 min recepies"', 'author': 'H. Lector'},
]


class IndexView(View):
    @csrf_exempt
    def get(self, request):
        return render(
            request,
            'articles/index.html',
            context={
                'articles': articles
            }
        )
