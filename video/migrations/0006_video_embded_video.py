# Generated by Django 3.1.4 on 2022-10-12 05:35

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0005_auto_20221011_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='embded_video',
            field=embed_video.fields.EmbedVideoField(default=None),
            preserve_default=False,
        ),
    ]