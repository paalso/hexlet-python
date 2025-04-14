from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    who = 'Paul'
    description = f'Articles for {who}'
    return render(request, 'index.html',context={
        'who': who,
        'description': description
    })


def subarticle(request):
    return HttpResponse('subarticle')


