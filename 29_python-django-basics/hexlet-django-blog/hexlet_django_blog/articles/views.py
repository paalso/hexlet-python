from django.http import Http404
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views import View
from .models import Article


# @csrf_exempt
class IndexView(View):
    template_name = "articles/index.html"

    def get(self, request, *args, **kwargs):
        return self._render_articles()

    def post(self, request, *args, **kwargs):
        article_data = {
            'title': request.POST.get('title'),
            'author': request.POST.get('author'),
        }
        Article.objects.create(**article_data)
        return self._render_articles()

    def _render_articles(self, items_on_page=15):
        articles = Article.objects.all()[:items_on_page]
        return render(
            self.request,
            self.template_name,
            context={"articles": articles},
        )


@require_http_methods(['GET'])
def articles_view(request, id):
    # BEGIN (write your solution here)
    article = Article.objects.get(id=id)
    if not article:
        raise Http404()
    # END
    return render(request, 'articles/article.html', context={'article': article})
