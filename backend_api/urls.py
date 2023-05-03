from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static 
# For the API
urlpatterns = [path("users/", views.Users.as_view(), name="users" ),
               path("users/<int:id>/", views.ProfileView.as_view(), name="userShowPage")
               ] 
