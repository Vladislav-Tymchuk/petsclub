# Generated by Django 4.0 on 2022-01-26 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
        ('mainPets', '0003_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Followers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followedPerson', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Пользователь', to='authentication.customuser')),
                ('followerPerson', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Подписавшийся', to='authentication.customuser')),
            ],
        ),
    ]