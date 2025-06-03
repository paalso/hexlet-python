from django.urls import path
from python_django_orm_blog import views

urlpatterns = [
    path('', views.index, name='index'),
]
