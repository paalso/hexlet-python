from django.urls import include, path
from simple_journal import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('articles/', include('simple_journal.articles.urls')),
    path('categories/', include('simple_journal.categories.urls')),
]
