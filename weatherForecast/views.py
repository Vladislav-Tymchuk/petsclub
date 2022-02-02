from django.shortcuts import redirect, render

from .models import WeatherViewer

def weatherMain(request, username):

    context = {}
    context['registered'] = False

    try:
        person = WeatherViewer.objects.get(weatherViewer = request.user)
        context['registered'] = True
    except:
        context['registered'] = False
        return redirect('set-addresses', username = request.user.username)

    return render(request, 'weather-main.html')


def setAddresses(request, username):

    return render(request, 'set-addresses.html')