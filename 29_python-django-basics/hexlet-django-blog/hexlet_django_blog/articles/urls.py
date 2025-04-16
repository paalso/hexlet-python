from django.urls import path

from hexlet_django_blog.articles import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='articles_index'),
    path('<str:tag>/<int:article_id>/', views.article, name='articles_show'),
    path('subarticle/', views.subarticle),
]
