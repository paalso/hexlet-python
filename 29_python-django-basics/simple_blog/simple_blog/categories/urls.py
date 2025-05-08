from django.urls import path
from simple_blog.categories import views

app_name = 'categories'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
