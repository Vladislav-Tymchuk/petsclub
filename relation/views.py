from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from authentication.models import CustomUser
from mainPets.models import Post
from .models import Followers, Like

def followPerson(request, follower, followed):

    followedPersonProfile = CustomUser.objects.get(username = followed)
    followerPersonRequest = CustomUser.objects.get(username = follower)

    try:
        Followers.objects.get(followedPerson = followedPersonProfile, followerPerson = followerPersonRequest)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except:
        Followers.objects.create(followedPerson = followedPersonProfile, followerPerson = followerPersonRequest)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def unfollowPerson(request, follower, followed):

    followedPersonProfile = CustomUser.objects.get(username = followed)
    followerPersonRequest = CustomUser.objects.get(username = follower)
    relation = get_object_or_404(Followers, followedPerson = followedPersonProfile, followerPerson = followerPersonRequest)
    relation.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def likePost(request, username, pk):

    post = Post.objects.get(id = pk)
    person = request.user

    try:
        Like.objects.get(likedPost = post, likedPerson = person)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except:
        Like.objects.create(likedPost = post, likedPerson = person)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def unlikePost(request, username, pk):

    post = Post.objects.get(id = pk)
    person = request.user

    try:
        like = Like.objects.get(likedPost = post, likedPerson = person)
        like.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except:
        pass

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
