from django.shortcuts import render
from rest_framework.views import APIView
from .models import User, Profile, Song, Artist, Playlist, Album
from .serializers import UserSerializer, ProfileSerializer, SongSerializer, ArtistSerializer, PlaylistSerializer, AlbumSerializer, RegisterSerializer
from django.http import JsonResponse
# Create your views here.
# get the data as a database as a json and use it in the frontend 

class Users(APIView):
    def get(self, requests):
        data = User.objects.all() 
        serializer = UserSerializer(data, many=True) #complex data to simple data
        return JsonResponse(serializer.data, safe=False)

class AllProfiles(APIView):
    def get(self, requests):
        data = Profile.objects.all()
        serializer=ProfileSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

class ProfileView(APIView):
    def get(self, requests, id):
        data = Profile.objects.all().filter(user_id=id) #user_id because I use a OneToOneField in the views.py 
        serializer = ProfileSerializer(data, many=True) 
        return JsonResponse(serializer.data, safe=False)
    
    def post(self, requests, id): 
        requests.data["user"] = id #create a user with the id
        serializer = ProfileSerializer(data=requests.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(serializer.errors)
    
    def put(self, requests, id):
        data = Profile.objects.get(user_id=id)
        serializer = ProfileSerializer(data, data=requests.data) #replace the old data with the new.
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(serializer.errors)




class AllSongs(APIView):
    def get(self, request):
        data = Song.objects.all()
        serializer = SongSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)
    
class SongView(APIView):
    def get(self, request, id):
        data = Song.objects.filter(id=id)
        serializer = SongSerializer(data, many=True)

class AllArtists(APIView):
    def get(self, requests):
        data = Artist.objects.all()
        serializer = ArtistSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

# Create the view for one artist        
class ArtistView(APIView):
    def get(self, requests, id):
        data = Artist.objects.all().filter(id=id)
        serializer = ArtistSerializer(data, many=True) 
        return JsonResponse(serializer.data, safe=False)

class AllPlaylists(APIView):
    def get(self, requests):
        data = Playlist.objects.all()
        serializer = PlaylistSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)
    
class AllAlbums(APIView):
    def get(self, request):
        data = Album.objects.all()
        serializer = AlbumSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

class AlbumView(APIView):
    def get(self, request, id):
        data = Album.objects.filter(id=id)
        serializer = AlbumSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

class RegisterView(APIView):
    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(serializer.errors)


