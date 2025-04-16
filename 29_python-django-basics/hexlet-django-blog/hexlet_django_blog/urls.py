from django.contrib import admin
from django.urls import include, path

from hexlet_django_blog import views

urlpatterns = [
    path('', views.HomePageView.as_view()),
    path('index/', views.HomePageView.as_view()),
    path('about/', views.about),
    path('articles/', include('hexlet_django_blog.articles.urls')),
    path('foobar/', views.foobar),
    path('users/<int:user_id>/pets/<int:pet_id>/med_info/', views.med_info_view),
    path('admin/', admin.site.urls),
    path('spec-page-1/', views.SpecialPage1.as_view()),
]
