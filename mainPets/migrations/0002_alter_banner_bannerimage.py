# Generated by Django 4.0 on 2021-12-25 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainPets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='bannerImage',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
