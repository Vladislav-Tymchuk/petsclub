from django.shortcuts import redirect, render
import requests
from geopy.geocoders import Nominatim
from bs4 import BeautifulSoup
from weatherForecast.forms import WeatherViewerEditForm, WeatherViewerForm

from .models import WeatherViewer

def weatherMain(request, username):

    context = {'weatherCity': {'weatherTodayDegree': 0, 'weatherTodayDescription': '', 'weatherTodayWindSpeed': '',
                           'weatherTomorrowDegree': 0, 'weatherTomorrowDescription': '', 'fullAddress': ''},
           'weatherCountry': {'weatherTodayDegree': 0, 'weatherTodayDescription': '', 'weatherTodayWindSpeed': '',
                             'weatherTomorrowDegree': 0, 'weatherTomorrowDescription': '', 'fullAddress': ''},
            'registered': True, 'weatherViewer': '', 'cityAddress': False, 'countryAddress': False}

    try:
        weatherViewer = WeatherViewer.objects.get(weatherViewer = request.user)
        context['weatherViewer'] = weatherViewer
    except:
        context['registered'] = False
        return redirect('set-addresses', username = request.user.username)

    def checkWeather(locationType, address):

        geolocator = Nominatim(user_agent="my_request")
        location = geolocator.geocode(address)
        url = f"https://yandex.ru/pogoda/?lat={location.latitude}&lon={location.longitude}&via=srp"
        webRequest = requests.get(url)

        data = BeautifulSoup(webRequest.text, 'lxml')
        weatherTemperatures = data.find_all('span', class_='temp__value temp__value_with-unit')

        weatherList = []
        for weatherTemperature in weatherTemperatures:
            weatherList.append(weatherTemperature.text)

        weatherTodayDegree = weatherList[1]
        weatherTomorrowDegree = weatherList[7]

        weatherTodayDescription = data.find('div', class_='link__condition day-anchor i-bem').text

        weatherDescriptions = data.find_all('div', class_='forecast-briefly__condition')
        desc = []
        for i in weatherDescriptions:
            desc.append(i.text)
        weatherTomorrowDescription = desc[2]

        weatherTodayWindSpeed = data.find('span', class_='wind-speed').text

        if locationType == 'city':

            context['weatherCity']['weatherTodayDegree'] = weatherTodayDegree
            context['weatherCity']['weatherTomorrowDegree'] = weatherTomorrowDegree
            context['weatherCity']['weatherTodayDescription'] = weatherTodayDescription
            context['weatherCity']['weatherTomorrowDescription'] = weatherTomorrowDescription
            context['weatherCity']['weatherTodayWindSpeed'] = weatherTodayWindSpeed
            context['weatherCity']['fullAddress'] = location.address

        elif locationType == 'country':

            context['weatherCountry']['weatherTodayDegree'] = weatherTodayDegree
            context['weatherCountry']['weatherTomorrowDegree'] = weatherTomorrowDegree
            context['weatherCountry']['weatherTodayDescription'] = weatherTodayDescription
            context['weatherCountry']['weatherTomorrowDescription'] = weatherTomorrowDescription
            context['weatherCountry']['weatherTodayWindSpeed'] = weatherTodayWindSpeed
            context['weatherCountry']['fullAddress'] = location.address

    if weatherViewer.weatherAddressCity:
        cityAddress = weatherViewer.weatherAddressCity
        context['cityAddress'] = True
        checkWeather('city', cityAddress)
    
    if weatherViewer.weatherAddressCity:
        countryAddress = weatherViewer.weatherAddressCountry
        context['countryAddress'] = True
        checkWeather('country', countryAddress)

    return render(request, 'weather-main.html', context)


def setAddresses(request, username):

    if request.method == 'POST':
        form = WeatherViewerForm(request.POST)
        if form.is_valid:
            weatherViewerForm = form.save(commit=False)
            weatherViewerForm.weatherViewer = request.user
            weatherViewerForm.save()
            return redirect('weather-forecast', username = request.user.username)

    else:
        form = WeatherViewerForm()

    context = {'form': form}

    return render(request, 'set-addresses.html', context)


def editAddresses(request, username):

    weatherViewerPerson = WeatherViewer.objects.get(weatherViewer = request.user)
    context = {'City': weatherViewerPerson.weatherAddressCity, 'Country': weatherViewerPerson.weatherAddressCountry}

    if request.method == 'POST':
        form = WeatherViewerEditForm(request.POST)
        if form.is_valid():
            weatherViewerEditForm = form.save(commit=False)
            weatherViewerPerson.weatherAddressCity = weatherViewerEditForm.weatherAddressCity
            weatherViewerPerson.weatherAddressCountry = weatherViewerEditForm.weatherAddressCountry
            weatherViewerPerson.save()
            return redirect('weather-forecast', username = request.user.username)
    else:
        form = WeatherViewerEditForm()

    return render(request, 'set-addresses.html', context)