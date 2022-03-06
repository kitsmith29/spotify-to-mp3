from django.urls import path
from .views import SignIn, Playlists, Tracks

urlpatterns = [
    path("", SignIn.as_view()),
    path("redirect/", Playlists.as_view()),
    path("tracks/", Tracks.as_view()),
]
