from django.urls import path
from simple_blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]
