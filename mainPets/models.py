from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

from authentication.models import CustomUser

class Banner(models.Model):
    bannerImage = models.ImageField(upload_to="images")
    bannerDescription = models.TextField(max_length=254)

    def __str__(self):
        return self.bannerDescription

class Pet(models.Model):
    
    petChoices = [
        ('Кошка', 'Кошка'),
        ('Кот', 'Кот'),
        ('Собака', 'Собака'),
        ('Пёс', 'Пёс'),
    ]
    pet = models.CharField(
        max_length=6,
        choices=petChoices,
        default='Кошка')
    petName = models.CharField(max_length=50)
    petOwner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    petBirthday = models.DateField()
    petPhoto = models.ImageField(upload_to='pet-images')
    petBio = models.TextField(max_length=511)

      
    def petAge(self):
        today = datetime.today()
        age = today.year - self.petBirthday.year - ((today.month, today.day) < (self.petBirthday.month, self.petBirthday.day))

        return age

    def smartAge(self):
        age = self.petAge()

        result = ''

        if age < 1:
            result = 'меньше года'
        elif age == 1:
            result =  str(age) + ' год'
        elif age == 2 or age == 3 or age == 4:
            result = str(age) + ' года'
        elif age > 4 and age < 21:
            result = str(age) + ' лет'
       
        return result
        
    def __str__(self):
        
        return (self.pet + ' ' + self.petName + ' ' + str(self.petAge()))