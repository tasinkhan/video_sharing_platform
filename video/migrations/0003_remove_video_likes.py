# Generated by Django 3.1.4 on 2022-10-11 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0002_video_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='likes',
        ),
    ]
