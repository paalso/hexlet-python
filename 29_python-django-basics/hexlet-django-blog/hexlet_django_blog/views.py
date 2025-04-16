from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse


def about(request):
    tags = ['обучение', 'программирование', 'python', 'oop']
    return render(
        request,
        'about.html',
        context={'tags': tags},
    )

# For roots like:
# /users/42/pets/101/med_info/
def med_info_view(request, user_id, pet_id):
    response = f'Yout requested user_id: {user_id}, pet_id: {pet_id} med info'
    return HttpResponse(response)


def foobar(request):
    return HttpResponse('Foo! Bar!!!')


class HomePageView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'World!!!'
        return context


class SpecialPage1(TemplateView):
    template_name = "special_template_1.html"
