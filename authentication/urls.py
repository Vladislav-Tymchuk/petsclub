from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.authenticationView, name='authentication'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('<int:pk>/edit/', views.editView, name='edit'),
    path('change-password/', views.ChangePasswordView.as_view(), name='change-password')
]