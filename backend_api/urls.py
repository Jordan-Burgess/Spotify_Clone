from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static 
# For the API

urlpatterns = [
    path("users/", views.Users.as_view(), name="users" ),
    path("profiles/", views.AllProfiles.as_view(), name="profiles"),
    path("users/<int:id>/", views.ProfileView.as_view(), name="userShowPage"),
    path("songs/", views.AllSongs.as_view(), name="songs"),
    path("songs/<int:id>/", views.SongView.as_view(), name="songShowPage"),
    path("artists/", views.AllArtists.as_view(), name="artists"),
    path("artists/<int:id>/", views.ArtistView.as_view(), name="oneArtistShowPage"),
    path("playlists/", views.AllPlaylists.as_view(), name="playlists"),
    path("albums/", views.AllAlbums.as_view(), name="allAlbums"),
    path("albums/<int:id>/", views.AlbumView.as_view(), name="albumShow"),
    path("register/", views.RegisterView.as_view(), name="registerShow"),
    path("createprofile/<int:id>/", views.ProfileView.as_view(), name="createProfile")
    
] 
