from .models import User, Profile, Song, Artist, Playlist, Album
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = "__all__"
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta():
        model = Profile
        fields = "__all__"
        
class SongSerializer(serializers.ModelSerializer):
    class Meta():
        model = Song
        
class ArtistSerializer(serializers.ModelSerializer):
    class Meta():
        model = Artist
        fields = "__all__"

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta():
        model = Playlist
        fields = "__all__"

class AlbumSerializer(serializers.ModelSerializer):
    class Meta():
        model = Album
        fields = "__all__"