# Generated by Django 4.2.1 on 2023-05-04 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0012_song_artists_alter_artist_banner_pic_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='playlists',
        ),
        migrations.AddField(
            model_name='profile',
            name='playlists',
            field=models.ManyToManyField(null=True, to='backend_api.playlist'),
        ),
    ]
