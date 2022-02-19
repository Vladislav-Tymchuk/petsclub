from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-pet', views.addPetView, name='add-pet'),
    path('<str:username>/edit-pet/<int:pk>', views.editPet, name='edit-pet'),
    path('profile/<str:username>/', views.checkProfile, name='profile'),
    path('pet/<int:petId>/<str:petName>/', views.petProfile, name='pet-profile'),
    path('<str:username>/posts/<slug:postSlug>/', views.fullPost, name='full-post'),
    path('<str:username>/create-post/', views.createPost, name='create-post'),
    path('<str:username>/edit-post/<slug:postSlug>', views.editPost, name='edit-post'),
    path('<str:username>/subscriptions', views.subscriptionsView, name='subscriptions'),
    path('<str:username>/delete-post/<slug:postSlug>', views.deletePost, name='delete-post'),
    path('comment/<int:pk>/delete/', views.deleteComment, name='delete-comment'),
    path('weather-forecast/', include('weatherForecast.urls')),
    path('relation/', include('relation.urls')),
    path('authentication/', include('authentication.urls')),
]