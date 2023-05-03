# Generated by Django 4.2.1 on 2023-05-03 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0006_alter_profile_profilepic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('length', models.IntegerField()),
                ('release_date', models.DateTimeField(auto_now_add=True)),
                ('lyrics', models.TextField()),
                ('media_mp3', models.FileField(upload_to='songs/')),
            ],
        ),
    ]