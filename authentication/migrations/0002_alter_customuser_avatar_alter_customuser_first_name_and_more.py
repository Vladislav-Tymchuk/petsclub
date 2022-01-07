# Generated by Django 4.0 on 2022-01-07 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.FileField(upload_to='avatars'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.TextField(blank=True, max_length=50),
        ),
    ]
