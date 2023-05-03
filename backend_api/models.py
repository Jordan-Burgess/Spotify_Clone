from django.db import models
from django.contrib.auth.models import User 

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #first field inherited from the User model from django
    country = models.CharField(max_length=500) 
    display_name = models.CharField(max_length=500)
    isPremium = models.BooleanField()
    profilePic = models.ImageField(null=True, blank=True, upload_to="profile_pictures/")

    def __str__(self):
        return self.user.username
    

class Song(models.Model):
    title = models.CharField(max_length=500)
    length = models.IntegerField()
    release_date = models.DateTimeField(auto_now_add=True)
    lyrics = models.TextField()
    media_mp3 = models.FileField(upload_to="songs/")

    def __str__(self):
        return self.title
