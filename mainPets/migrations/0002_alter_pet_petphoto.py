# Generated by Django 4.0 on 2022-01-10 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainPets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='petPhoto',
            field=models.ImageField(blank=True, null=True, upload_to='pet-images'),
        ),
    ]
