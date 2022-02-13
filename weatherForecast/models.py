from django.db import models

from authentication.models import CustomUser

class WeatherViewer(models.Model):

    weatherViewer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    weatherAddressCity = models.TextField(max_length=127, null=True, blank=True)
    weatherAddressCountry = models.TextField(max_length=127, null=True, blank=True)

    def __str__(self):
        if self.weatherAddressCity:
            return self.weatherAddressCity
        elif self.weatherAddressCountry:
            return self.weatherAddressCountry
        else:
            return 'Строка'