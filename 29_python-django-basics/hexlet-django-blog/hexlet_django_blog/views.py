from django.shortcuts import render
from django.views.generic.base import TemplateView


def about(request):
    tags = ['обучение', 'программирование', 'python', 'oop']
    return render(
        request,
        'about.html',
        context={'tags': tags},
    )


class HomePageView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'World!!!'
        return context


class SpecialPage1(TemplateView):
    template_name = "special_template_1.html"
