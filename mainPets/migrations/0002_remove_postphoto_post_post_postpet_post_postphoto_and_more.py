# Generated by Django 4.0 on 2022-01-15 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainPets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postphoto',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='postPet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainPets.pet'),
        ),
        migrations.AddField(
            model_name='post',
            name='postPhoto',
            field=models.ImageField(blank=True, null=True, upload_to='posts-images'),
        ),
        migrations.DeleteModel(
            name='PostPet',
        ),
        migrations.DeleteModel(
            name='PostPhoto',
        ),
    ]
