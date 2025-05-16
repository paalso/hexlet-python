from django.urls import path
from simple_blog.categories import views

# app_name = 'categories'

urlpatterns = [
    path('', views.IndexView.as_view(), name='categories_index'),
    path('<int:id>/update/', views.CategoryFormUpdateView.as_view(), name='categories_update'),
    path('<int:id>/', views.CategoryView.as_view(), name='categories_detail'),
    path('create/', views.CategoryFormView.as_view(), name='categories_create'),
]
