from django.db import models
from django.contrib.auth.models import User 
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=500)
    followers = models.IntegerField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="artist_pictures/profile_pictures/")
    banner_pic = models.ImageField(null=True, blank=True, upload_to="artist_pictures/banner_pictures/")
    is_verified = models.BooleanField()

    def __str__(self):
        return self.name
    
class Album(models.Model):
    name = models.CharField(max_length=500)
    artists = models.ManyToManyField(Artist)
    release_year = models.IntegerField()
    genre = ArrayField(models.CharField(max_length=500))
    picture = models.ImageField(upload_to="album_images")

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=500)
    artists = models.ManyToManyField(Artist)
    length = models.IntegerField()
    release_date = models.DateTimeField(auto_now_add=True)
    lyrics = models.TextField()
    media_mp3 = models.FileField(upload_to="songs/")
    album = models.ForeignKey(Album, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Playlist(models.Model):
    name = models.CharField(max_length=500)
    playlist_image = models.ImageField(null=True, blank=True, upload_to="playlist_images/")
    description = models.CharField(max_length=300)
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.name
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #first field inherited from the User model from django
    country = models.CharField(max_length=500) 
    display_name = models.CharField(max_length=500)
    isPremium = models.BooleanField()
    profilePic = models.ImageField(null=True, blank=True, upload_to="profile_pictures/")
    artists = models.ManyToManyField(Artist) 
    playlists = models.ManyToManyField(Playlist)

    def __str__(self):
        return self.user.username



