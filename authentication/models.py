from django.contrib.auth.models import AbstractUser
from django.db import models
from django.shortcuts import redirect
from django.urls import reverse

class CustomUser(AbstractUser):
    avatar = models.FileField(upload_to='avatars', blank=True)
    username = models.TextField(max_length = 17, unique=True)
    first_name = models.TextField(max_length = 50, blank=True)
    last_name = models.TextField(max_length = 50, blank=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

    def fullName(self):

        return self.first_name + ' ' + self.last_name



    

