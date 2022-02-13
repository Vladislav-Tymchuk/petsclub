from .models import WeatherViewer
from django.forms.models import ModelForm

class WeatherViewerForm(ModelForm):

    class Meta:
        model = WeatherViewer
        fields = ['weatherAddressCity', 'weatherAddressCountry']


class WeatherViewerEditForm(ModelForm):

    class Meta:
        model = WeatherViewer
        fields = ['weatherAddressCity', 'weatherAddressCountry']