from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.authenticationView, name='authentication'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('edit/', views.editView, name='edit'),
]