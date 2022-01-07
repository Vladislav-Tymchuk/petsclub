# Generated by Django 4.0 on 2022-01-07 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bannerImage', models.ImageField(upload_to='images')),
                ('bannerDescription', models.TextField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet', models.CharField(choices=[('Кошка', 'Кошка'), ('Кот', 'Кот'), ('Собака', 'Собака'), ('Пёс', 'Пёс')], default='Кошка', max_length=6)),
                ('petName', models.CharField(max_length=50)),
                ('petBirthday', models.DateField()),
                ('petPhoto', models.ImageField(upload_to='pet-images')),
                ('petBio', models.TextField(max_length=511)),
                ('petOwner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.customuser')),
            ],
        ),
    ]
