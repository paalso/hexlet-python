from django.urls import path
from simple_blog.categories import views

app_name = 'categories'
urlpatterns = [
    path('', views.index, name='index'),
]
