from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-pet', views.addPetView, name='add-pet'),
    path('edit-pet/<int:pk>', views.editPet, name='edit-pet'),
    path('profile/<str:username>/', views.checkProfile, name='profile'),
    path('pet/<int:petId>/<str:petName>/', views.petProfile, name='pet-profile'),
    path('<str:username>/posts/<slug:postSlug>/', views.fullPost, name='full-post'),
    path('authentication/', include('authentication.urls')),
]