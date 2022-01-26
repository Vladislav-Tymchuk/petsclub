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
    path('<str:username>/delete-post/<slug:postSlug>', views.deletePost, name='delete-post'),
    path('comment/<int:pk>/delete/', views.deleteComment, name='delete-comment'),
    path('<str:follower>/follow/<str:followed>', views.followPerson, name='follow-person'),
    path('<str:follower>/unfollow/<str:followed>', views.unfollowPerson, name='unfollow-person'),
    path('authentication/', include('authentication.urls')),
]