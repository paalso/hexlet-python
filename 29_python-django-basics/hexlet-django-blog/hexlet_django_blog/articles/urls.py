from django.urls import path

from hexlet_django_blog.articles import views

urlpatterns = [
    path('', views.index),
    path('subarticle/', views.subarticle),
]
