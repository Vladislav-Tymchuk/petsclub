from django.urls import path, include
from . import views

urlpatterns = [
    path('<str:username>/', views.weatherMain, name='weather-forecast'),
    path('<str:username>/set-addresses/', views.setAddresses, name='set-addresses'),
]