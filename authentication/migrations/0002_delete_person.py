# Generated by Django 4.0 on 2021-12-29 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
    ]