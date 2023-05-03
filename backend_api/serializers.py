from .models import User, Profile, Song, Artist
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