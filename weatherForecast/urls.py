from django.urls import path, include
from . import views

urlpatterns = [
    path('<str:username>/', views.weatherMain, name='weather-forecast'),
    path('<str:username>/set-addresses/', views.setAddresses, name='set-addresses'),
    path('<str:username>/edit-addresses/', views.editAddresses, name='edit-addresses'),

]