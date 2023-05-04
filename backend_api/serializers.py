from .models import User, Profile, Song, Artist, Playlist, Album
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

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

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta():
        model = User
        fields = ("username","password", "password2", "email")
    
    def validate(self, attributes):
        if attributes["password"] != attributes["password2"]:
            raise serializers.ValidationError({ "password" : "The password didn't match"})
        else:
            return attributes
    
    def create(self, data):
        user = User.objects.create(username=data["username"], email=data["email"])
        user.set_password(data["password"])
        user.save()
        return user 
                
        
        

    
