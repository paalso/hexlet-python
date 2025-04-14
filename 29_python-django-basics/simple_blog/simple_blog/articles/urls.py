from django.urls import path
from simple_blog.articles import views

urlpatterns = [
    # path('', views.index, name='articles_index'),
    path('', views.IndexView.as_view(), name='articles_index'),
]
