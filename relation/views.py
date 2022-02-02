from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from authentication.models import CustomUser
from mainPets.models import Comment, Post
from .models import Followers, LikeComment, LikePost

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
        LikePost.objects.get(likedPost = post, likedPerson = person)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except:
        LikePost.objects.create(likedPost = post, likedPerson = person)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def unlikePost(request, username, pk):

    post = Post.objects.get(id = pk)
    person = request.user

    try:
        like = LikePost.objects.get(likedPost = post, likedPerson = person)
        like.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except:
        pass

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def likeComment(request, username, pk):

    comment = Comment.objects.get(id = pk)
    person = request.user

    try:
        LikeComment.objects.get(likedComment = comment, likedPerson = person)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except:
        LikeComment.objects.create(likedComment = comment, likedPerson = person)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def unlikeComment(request, username, pk):

    comment = Comment.objects.get(id = pk)
    person = request.user

    try:
        comment = LikeComment.objects.get(likedComment = comment, likedPerson = person)
        comment.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except:
        LikeComment.objects.create(likedComment = comment, likedPerson = person)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
