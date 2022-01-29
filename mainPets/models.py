import string
from tabnanny import verbose
from django.db import models
from datetime import datetime
from django.urls import reverse

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
    petPhoto = models.ImageField(upload_to='pet-images', blank=True, null=True)
    petBio = models.TextField(max_length=511)

    def petEdit(self):
        return reverse('edit-pet', kwargs={'username': self.petOwner, 'pk': self.id})

    def smallInfo(self):

        return self.petBio[:70]

    def petProfile(self):

        pet = Pet.objects.get(id = self.id)


        return reverse('pet-profile', kwargs={'petId': pet.id, "petName": pet.petName})


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

    def name(self):

        return (self.pet + ' ' + self.petName)
        
    def __str__(self):
        
        return (self.pet + ' ' + self.petName + ' ' + str(self.petAge()))


class Post(models.Model):

    postAuthor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    postTitle = models.CharField(max_length = 127)
    postText = models.TextField(max_length = 4095)
    postPet = models.ForeignKey(Pet, on_delete=models.CASCADE, blank=True, null=True)
    postPhoto = models.ImageField(upload_to='posts-images', blank=True, null=True)
    postSlug = models.SlugField(max_length = 70, unique=True)
    postTimePublished = models.TimeField(auto_now_add=True)
    postDatePublished = models.DateField(auto_now_add=True)

    def textToPreview(self):

        return self.postText[:70]

    def __str__(self):

        return self.postTitle

    def get_url(self):

        return reverse('full-post', kwargs={'username': self.postAuthor, 'postSlug': self.postSlug})

    def get_url_edit(self):

        return reverse('edit-post', kwargs={'username': self.postAuthor, 'postSlug': self.postSlug})

    def get_url_delete(self):

        return reverse('delete-post', kwargs={'username': self.postAuthor, 'postSlug': self.postSlug})

    def authorProfile(self):

        return reverse('profile', kwargs={'username': self.postAuthor})

    def petProfile(self):

        pet = Pet.objects.get(id = self.postPet.id)

        return reverse('pet-profile', kwargs={'petId': pet.id, "petName": pet.petName})

    
    class Meta:
        ordering = ['-postDatePublished']


class Comment(models.Model):

    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentAuthor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    commentText = models.TextField(max_length=127)
    commentTimePublished = models.TimeField(auto_now_add=True)
    commentDatePublished = models.DateField(auto_now_add=True)

    def __str__(self):

        return self.commentText

    
    def getCommentAuthor(self):

        return reverse('profile', args={'username': self.commentAuthor})

    
    class Meta:
        ordering = ['-commentDatePublished']