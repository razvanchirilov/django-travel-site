from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('tours/', views.tours, name='tours'),
    path('blog/', views.blog, name='blog'),
    path('contacts/', views.contacts, name='contacts'),
]