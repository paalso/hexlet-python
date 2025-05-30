from django.urls import path
from hexlet_django_blog.articles import views

app_name = 'articles'

urlpatterns = [
    path('', views.IndexView.as_view(), name='articles_index'),
    path('<int:id>/', views.articles_view, name='articles_view'),
]
