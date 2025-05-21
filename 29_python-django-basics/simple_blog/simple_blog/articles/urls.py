from django.urls import path
from simple_blog.articles import views

# app_name = 'articles'

urlpatterns = [
    path('', views.IndexView.as_view(), name='articles_index'),
    path('<int:id>/edit/', views.ArticleFormEditView.as_view(), name='articles_edit'),
    path('<int:id>/delete/', views.ArticleFormDeleteView.as_view(), name='articles_delete'),
    path('<int:id>/', views.ArticleView.as_view(), name='articles_detail'),
    path('create/', views.ArticleFormView.as_view(), name='articles_create'),
]
