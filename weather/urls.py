from django.urls import path
from weather import views

urlpatterns = [
    path('', views. index),
    path('about_news', views. about_news),
]
