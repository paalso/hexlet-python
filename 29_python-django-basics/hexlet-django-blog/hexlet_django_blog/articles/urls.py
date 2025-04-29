from django.urls import path
from hexlet_django_blog.articles import views

urlpatterns = [
    path('', views.index, name='articles_index'),
    path('<int:id>/', views.articles_view, name='articles_view'),
]
