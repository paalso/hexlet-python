from django.urls import path

from . import views
from simple_blog import views as root_views

urlpatterns = [
    path("", views.ArticleListView.as_view(), name="article_list"),
    path("<int:id>/", views.ArticleDetailView.as_view(), name="article_detail"),
    path("create/", views.ArticleCreate.as_view(), name="article_create"),
    path("hello/", root_views.hello_view),
]
