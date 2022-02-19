from poplib import POP3_SSL_PORT
from django.http import HttpResponseRedirect

from django.urls import reverse
from authentication.models import CustomUser
from django.shortcuts import get_object_or_404, redirect, render
from datetime import datetime
from datetime import date
from relation.models import Followers, LikePost
from transliterate import slugify

from .forms import CommentForm, PetAddForm, PetEditForm, PostEditForm, PostForm
from .models import Banner, Comment, Pet, Post


def home(request):

    bannerFirst = Banner.objects.all()[0]
    banners = Banner.objects.all()[1:]
    context = {
        'bannerFirst': bannerFirst,
        'banners': banners,
        'person': '',
        'pets': '',
        'followersCount': 0,
    }
    person = ''
    try:
        person = CustomUser.objects.get(id = request.user.id)
        pets = Pet.objects.filter(petOwner = person.id)
        context['person'] = person
        context['pets'] = pets
        context['petsCount'] = pets.count
    except Exception:
        pass

    posts = Post.objects.filter(postAuthor = request.user.id)
    context.update({'posts': posts})
    context.update({'postsCount': posts.count})

    try:
        followers = Followers.objects.filter(followedPerson = request.user)
        context['followersCount'] = followers.count
    except:
        context['followersCount'] = '-'
    
    return render(request, 'home.html', context=context)


def addPetView(request):

    if request.method == 'POST':
        form = PetAddForm(request.POST, request.FILES)       
        if form.is_valid():
            ancet = form.save(commit=False)
            ancet.petOwner = request.user
            ancet.save()
            return redirect('home')
    else:
        form = PetAddForm()

    return render(request, 'add-pet.html', {'form': form})

def editPet(request, username, pk):

    pet = Pet.objects.get(id = pk)

    if request.user != pet.petOwner:
        return redirect('home')
    
    if request.method == 'POST':
        
        PetForm = PetEditForm(request.POST, request.FILES, instance = pet)

        if PetForm.is_valid():
            PetForm.save()
            return redirect('home')
    else:
        PetForm = PetEditForm()
    

    return render(request, 'edit-pet.html', {'PetForm': PetForm, 'pet': pet})

def checkProfile(request, username):

    context = {
        'followersCount': 0,
        'marker': False, # True if request.user is a follower for profile page user
    }

    person = get_object_or_404(CustomUser, username = username)

    if person.username == request.user.username:
        return redirect('home')

    try:
        Followers.objects.get(followedPerson = person.id, followerPerson = request.user)
        context['marker'] = True
    except:
        context['marker'] = False


    pets = Pet.objects.filter(petOwner = person.id)
    context.update({'person': person})
    context.update({'pets': pets})
    context.update({'petsCount': pets.count})

    posts = Post.objects.filter(postAuthor = person.id)
    context.update({'posts': posts})
    context.update({'postsCount': posts.count})

    try:
        followers = Followers.objects.filter(followedPerson = person.id)
        context['followersCount'] = followers.count
    except:
        pass

    

    return render(request, 'profile.html', context)


def petProfile(request, petId, petName):

    context = {}

    pet = Pet.objects.get(id = petId)
    context.update({'pet': pet})

    posts = Post.objects.filter(postPet = petId)
    context.update({'posts': posts})

    return render(request, 'pet-profile.html', context)


def fullPost(request, username, postSlug):

    context = {}
    context['marker'] = False
    context['comments'] = {}

    post = Post.objects.get(postSlug = postSlug)
    comments = ''
    try:
        comments = Comment.objects.filter(commentPost = post)
    except:
        pass

    try: 
        likesPost = LikePost.objects.filter(likedPost = post.id)
        likesPostCount = likesPost.count
    except:
        likesPostCount = 0

    try:
        LikePost.objects.get(likedPost = post.id, likedPerson = request.user)
        context['marker'] = True
    except:
        context['marker'] = False

    context.update({'post': post})
    context.update({'comments': comments})
    context['likesPostCount'] = likesPostCount

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():

            comment = form.save(commit=False)
            comment.commentAuthor = request.user

            now = datetime.now()  
            currentTime = now.strftime("%H:%M:%S")
            comment.commentTimePublished = currentTime

            today = date.today()
            comment.commentDatePublished = today.strftime('Y-m-d')

            comment.commentPost = post

            comment.save()
            return redirect('full-post', username = post.postAuthor, postSlug = post.postSlug)
    else:
        form = CommentForm()
        context.update({'form': form})

    return render(request, 'full-post.html', context)


def createPost(request, username):

    context = {}
    pets = Pet.objects.filter(petOwner = request.user)
    context.update({'pets': pets})

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.postAuthor = request.user

            now = datetime.now()  
            currentTime = now.strftime("%H:%M:%S")
            post.postTimePublished = currentTime

            today = date.today()
            post.postDatePublished = today.strftime('Y-m-d')

            text = post.postTitle
            slug = slugify(text)
            post.postSlug = slug

            post.save()
            return redirect('home')
    else:
        form = PostForm()


    return render(request, 'create-post.html', context)


def editPost(request, username, postSlug):

    context = {}

    post = Post.objects.get(postSlug = postSlug)
    if request.user != post.postAuthor:
        return redirect('home')

    context.update({'post': post})

    pets = Pet.objects.filter(petOwner = request.user)
    context.update({'pets': pets})

    if request.method == 'POST':

        form = PostEditForm(request.POST, request.FILES)

        if form.is_valid():

            newPost = form.save(commit=False)
            post.postTitle = newPost.postTitle
            post.postText = newPost.postText
            
            if newPost.postPhoto:
               post.postPhoto = newPost.postPhoto

            post.save() 

            return redirect('full-post', username = post.postAuthor, postSlug = post.postSlug)
    else:
        form = PostEditForm()
    
    
    return render(request, 'edit-post.html', context)


def subscriptionsView(request, username):

    context = {}
    person = CustomUser.objects.get(id = request.user.id)
    
    followedRelations = Followers.objects.filter(followerPerson = person)
    followedPersons = []

    for followedRelation in followedRelations:
        followedPersons.append(CustomUser.objects.get(id = followedRelation.followedPerson.id))

    followedPosts = []
    for followedPerson in followedPersons:
        posts = Post.objects.filter(postAuthor = followedPerson)
        for post in posts:
            followedPosts.append(post)
    
    context.update({'followedPosts': followedPosts})
    context.update({'followedPersons': followedPersons})
    return render(request, 'subscriptions.html', context)


def deletePost(request, username, postSlug):

    post = Post.objects.get(postSlug = postSlug)

    if request.user != post.postAuthor:
        return redirect('home')
        
    post.delete()

    return redirect('home')


def deleteComment(request, pk):

    comment = Comment.objects.get(id = pk)
    post = comment.commentPost

    if request.user != comment.commentAuthor:
        return redirect('home')

    comment.delete()

    return redirect('full-post', username = post.postAuthor, postSlug =  post.postSlug)