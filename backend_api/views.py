from django.shortcuts import render
from rest_framework.views import APIView
from .models import User, Profile
from .serializers import UserSerializer, ProfileSerializer
from django.http import JsonResponse
# Create your views here.
# get the data as a database as a json and use it in the frontend 

class Users(APIView):
    def get(self, requests):
        data = User.objects.all() #
        serializer = UserSerializer(data, many=True) #complex data to simple data
        return JsonResponse(serializer.data, safe=False)

class ProfileView(APIView):
    def get(self, requests, id):
        print(Profile.objects.all())
        data = Profile.objects.all().filter(user_id=id) #user_id because I use a OneToOneField in the views.py 
        serializer = ProfileSerializer(data, many=True) #complex data to simple data
        return JsonResponse(serializer.data, safe=False)
