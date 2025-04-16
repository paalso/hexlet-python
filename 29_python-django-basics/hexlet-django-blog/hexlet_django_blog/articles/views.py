from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View


def subarticle(request):
    return HttpResponse('subarticle')


def article(request, tag, article_id):
    response = f'Статья номер {article_id}. Тег {tag}'
    return HttpResponse(response)


class IndexView(View):
    def get(self, request):
        who = 'Paul'
        description = f'Articles for {who}'
        return render(
            request,
            'articles/index.html', context={
            'who': who,
            'description': description
        })

