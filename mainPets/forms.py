from dataclasses import fields
from django import forms
from django.forms.models import ModelForm
from django.http import request
from django.shortcuts import get_object_or_404

from authentication.models import CustomUser
from .models import Pet

class PetAddForm(ModelForm):

    petChoices = [
        ('Кошка', 'Кошка'),
        ('Кот', 'Кот'),
        ('Собака', 'Собака'),
        ('Пёс', 'Пёс'),
    ]
    pet = forms.ChoiceField(choices=petChoices)
    petName = forms.CharField(max_length=50)
    petPhoto = forms.ImageField()
    petBirthday = forms.DateField()
    petBio = forms.CharField(max_length=511)

    class Meta:
        model = Pet
        fields = ['pet', 'petName', 'petBirthday', 'petPhoto', 'petBio']


class PetEditForm(ModelForm):

    petChoices = [
        ('Кошка', 'Кошка'),
        ('Кот', 'Кот'),
        ('Собака', 'Собака'),
        ('Пёс', 'Пёс'),
    ]
    pet = forms.ChoiceField(choices=petChoices)
    petName = forms.CharField(max_length=50)
    petBirthday = forms.DateField()
    petBio = forms.CharField(max_length=511)

    class Meta:
        model = Pet
        fields = ['pet', 'petName', 'petBirthday', 'petBio']