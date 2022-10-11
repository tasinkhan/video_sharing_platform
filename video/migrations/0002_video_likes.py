# Generated by Django 3.1.4 on 2022-10-11 15:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='likes',
            field=models.ManyToManyField(related_name='video_like', to=settings.AUTH_USER_MODEL),
        ),
    ]