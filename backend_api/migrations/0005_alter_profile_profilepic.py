# Generated by Django 4.2.1 on 2023-05-03 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0004_alter_profile_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profilePic',
            field=models.ImageField(storage='../media/', upload_to='profile_pictures/'),
        ),
    ]
