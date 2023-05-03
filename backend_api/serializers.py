from .models import User, Profile, Song
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
        fields = "__all__"