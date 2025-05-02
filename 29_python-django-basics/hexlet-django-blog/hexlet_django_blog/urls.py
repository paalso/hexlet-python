from django.contrib import admin
from django.urls import include, path
from hexlet_django_blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('articles/', include('hexlet_django_blog.articles.urls')),
    path('categories/', include('hexlet_django_blog.categories.urls')),
    path('admin/', admin.site.urls),
]
