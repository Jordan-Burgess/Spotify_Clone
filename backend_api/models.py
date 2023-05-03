from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=500)
    followers = models.IntegerField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="artist_pictures/profile_pictures/")
    banner_pic = models.ImageField(null=True, blank=True, upload_to="artist_pictures/banner_pictures/")
    is_verified = models.BooleanField()

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #first field inherited from the User model from django
    country = models.CharField(max_length=500) 
    display_name = models.CharField(max_length=500)
    isPremium = models.BooleanField()
    profilePic = models.ImageField(null=True, blank=True, upload_to="profile_pictures/")

    artists = models.ManyToManyField(Artist) 

    def __str__(self):
        return self.user.username
