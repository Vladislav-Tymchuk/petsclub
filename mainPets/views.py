from poplib import POP3_SSL_PORT

from django.urls import reverse
from authentication.models import CustomUser
from django.shortcuts import get_object_or_404, redirect, render
from datetime import datetime
from datetime import date
from transliterate import slugify

from .forms import PetAddForm, PetEditForm, PostEditForm, PostForm
from .models import Banner, Pet, Post


def home(request):

    bannerFirst = Banner.objects.all()[0]
    banners = Banner.objects.all()[1:]
    context = {
        'bannerFirst': bannerFirst,
        'banners': banners,
        'person': '',
        'pets': '',
    }
    person = ''
    try:
        person = CustomUser.objects.get(id = request.user.id)
        pets = Pet.objects.filter(petOwner = person.id)
        context['person'] = person
        context['pets'] = pets
    except Exception:
        pass

    posts = Post.objects.filter(postAuthor = request.user.id)
    context.update({'posts': posts})
    
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

    }

    person = get_object_or_404(CustomUser, username = username)
    pets = Pet.objects.filter(petOwner = person.id)
    context.update({'person': person})
    context.update({'pets': pets})

    posts = Post.objects.filter(postAuthor = person.id)
    context.update({'posts': posts})

    if person.username == request.user.username:
        return redirect('home')
    

    return render(request, 'profile.html', context=context)


def petProfile(request, petId, petName):

    context = {}

    pet = Pet.objects.get(id = petId)
    context.update({'pet': pet})

    posts = Post.objects.filter(postPet = petId)
    context.update({'posts': posts})

    return render(request, 'pet-profile.html', context)


def fullPost(request, username, postSlug):

    context = {}

    post = Post.objects.get(postSlug = postSlug)

    context.update({'post': post})

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


def deletePost(request, username, postSlug):

    post = Post.objects.get(postSlug = postSlug)
    post.delete()

    return redirect('home')