from django.contrib import admin
from .models import Profile, Song, Artist, Playlist

# The User model is already imported from Django

# Register your models here.
admin.site.register(Profile)
admin.site.register(Song)
admin.site.register(Artist)
admin.site.register(Playlist)