from django.shortcuts import render
from .models import Banner


def home(request):
    bannerFirst = Banner.objects.all()[0]
    banners = Banner.objects.all()[1:]


    context = {
        'bannerFirst': bannerFirst,
        'banners': banners,
    }
    return render(request, 'home.html', context=context)
