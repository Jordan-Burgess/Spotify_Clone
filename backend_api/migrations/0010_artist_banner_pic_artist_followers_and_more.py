# Generated by Django 4.2.1 on 2023-05-03 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0009_artist_delete_artists_profile_artists'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='banner_pic',
            field=models.ImageField(blank=True, null=True, upload_to='banner_pictures/'),
        ),
        migrations.AddField(
            model_name='artist',
            name='followers',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artist',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/'),
        ),
    ]
