from authentication.models import CustomUser
from django.shortcuts import get_object_or_404, render
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
