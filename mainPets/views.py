from poplib import POP3_SSL_PORT
from authentication.models import CustomUser
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PetAddForm, PetEditForm
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
    # обработать хозяина питомца
    if request.method == 'POST':
        form = PetAddForm(request.POST, files=(request.FILES or None))
        if form.is_valid():
            
            fPet = PetAddForm(request.POST, request.FILES)
            pet = form.cleaned_data['pet']
            petName = request.POST.get('petName')
            petOwner = CustomUser.objects.get(username = request.user.username)
            petBirthday = request.POST.get('petBirthday')
            petPhoto = request.POST.get('petPhoto')
            petBio = request.POST.get('petBio')
            fPet = Pet.objects.create(pet = pet, petName = petName, petOwner = petOwner, petBirthday = petBirthday, petPhoto = petPhoto,
                petBio = petBio)
            fPet.save()
            
            return redirect('home')
    else:
        form = PetAddForm()

    return render(request, 'add-pet.html', {'form': form})

def editPet(request, pk):

    pet = Pet.objects.get(id = pk)
    
    if request.method == 'POST':
        
        PetForm = PetEditForm(request.POST, instance = pet)

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