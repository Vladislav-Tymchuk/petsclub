from authentication.models import CustomUser
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PetAddForm, PetEditForm
from .models import Banner, Pet


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
    
    return render(request, 'home.html', context=context)


def addPetView(request):
    # обработать хозяина питомца
    if request.method == 'POST':
        form = PetAddForm(request.POST, request.FILES)
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