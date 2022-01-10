from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-pet', views.addPetView, name='add-pet'),
    path('edit-pet/<int:pk>', views.editPet, name='edit-pet'),
    path('authentication/', include('authentication.urls')),
]