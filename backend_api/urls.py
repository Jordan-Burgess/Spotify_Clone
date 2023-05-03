from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static 
# For the API

urlpatterns = [
    path("users/", views.Users.as_view(), name="users" ),
    path("users/<int:id>/", views.ProfileView.as_view(), name="userShowPage"),
    path("songs/", views.AllSongs.as_view(), name="songs"),
    path("songs/<int:id>/", views.SongView.as_view(), name="songShowPage"),
    path("artists/", views.AllArtists.as_view(), name="allArtists"),
    path("artists/<int:id>/", views.ArtistView.as_view(), name="oneArtistShowPage"),
] 
