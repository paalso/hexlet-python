from django.urls import path
from simple_blog.articles import views


app_name = 'articles'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:id>', views.ArticleView.as_view(), name='article'),
]
