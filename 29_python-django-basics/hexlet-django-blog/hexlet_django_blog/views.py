from django.shortcuts import render
from django.conf import settings

TEAM = [
    {'name': 'Yoda', 'position': 'CEO'},
    {'name': 'Obi-Wan Kenobi', 'position': 'Senior Developer'},
    {'name': 'Anakin Skywalker', 'position': 'Junior Developer'},
    {'name': 'Jar Jar Binks', 'position': 'Trainee'},
]


def index(request):
    print(settings.USERNAME)
    return render(
        request,
        'index.html',
        context={
            'username': settings.USERNAME,
            'password': settings.PASSWORD,
            }
    )

def about(request):
    return render(request, 'about.html')


def articles(request):
    return render(request, 'articles/index.html', context={'articles':{}})
