from django.contrib.auth.models import AbstractUser
from django.db import models
from django.shortcuts import redirect
from PIL import Image

class CustomUser(AbstractUser):
    avatar = models.FileField(upload_to='avatars', blank=True)
    username = models.TextField(max_length = 17, unique=True)
    first_name = models.TextField(max_length = 50, blank=True)
    last_name = models.TextField(max_length = 50, blank=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return redirect('home')

    def save(self, *args, **kwargs):
        super().save()
        if self.avatar:

            img = Image.open(self.avatar.path)

            if img.height > 100 or img.width > 100:
                new_img = (100, 100)
                img.thumbnail(new_img)
                img.save(self.avatar.path)



    

