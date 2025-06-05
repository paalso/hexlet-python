from django.urls import path

from . import views
from simple_blog import views as root_views

urlpatterns = [
    path("", views.ArticleListView.as_view(), name="article_list"),
    path("<int:id>/update/", views.ArticleUpdateView.as_view(), name="article_update"),
    path("<int:id>/delete/", views.ArticleDeleteView.as_view(), name="article_delete"),
    path("<int:id>/", views.ArticleDetailView.as_view(), name="article_detail"),
    path("create/", views.ArticleCreateView.as_view(), name="article_create"),
]
