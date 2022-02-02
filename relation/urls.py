from django.urls import path, include
from . import views

urlpatterns = [
    path('<str:follower>/follow/<str:followed>', views.followPerson, name='follow-person'),
    path('<str:follower>/unfollow/<str:followed>', views.unfollowPerson, name='unfollow-person'),
    path('<str:username>/like/post/<int:pk>', views.likePost, name='like-post'),
    path('<str:username>/unlike/post/<int:pk>', views.unlikePost, name='unlike-post'),
    path('<str:username>/like/comment/<int:pk>', views.likeComment, name='like-comment'),
    path('<str:username>/unlike/comment/<int:pk>', views.unlikeComment, name='unlike-comment'),
]