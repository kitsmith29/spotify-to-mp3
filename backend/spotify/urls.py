from django.urls import path
from .views import SignIn, Playlists

urlpatterns = [
    path("", SignIn.as_view()),
    path("redirect/", Playlists.as_view()),
]
