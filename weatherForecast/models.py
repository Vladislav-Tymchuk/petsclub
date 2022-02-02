from django.db import models

from authentication.models import CustomUser

class WeatherViewer(models.Model):

    weatherViewer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    weatherAddressCity = models.TextField(max_length=127)
    weatherAddressCountry = models.TextField(max_length=127)
