from decouple import config
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import redirect
import spotipy
from django.http import HttpResponse

CLIENT_ID = config("CLIENT_ID")
CLIENT_SECRET = config("CLIENT_SECRET")
REDIRECT_URI = config("REDIRECT_URI")

scope = "playlist-read-collaborative playlist-read-private"


class SignIn(APIView):
    def get(self, request):
        sp_auth = spotipy.SpotifyOAuth(
            scope=scope,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URI,
        )

        redirect_url = sp_auth.get_authorize_url()
        return redirect(redirect_url)


class Playlists(APIView):
    def get(self, request):
        sp_auth = spotipy.SpotifyOAuth(
            scope=scope,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URI,
        )

        code = request.GET.get("code", "")
        token = sp_auth.get_access_token(code=code)
        sp = spotipy.Spotify(auth=token["access_token"])
        results = sp.current_user_playlists()

        return Response(results)


class Tracks(APIView):
    def get(self, request):
        sp_auth = spotipy.SpotifyOAuth(
            scope=scope,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URI,
        )

        code = request.GET.get("code", "")
        token = sp_auth.get_access_token(code=code)
        sp = spotipy.Spotify(auth=token["access_token"])

        playlist_id = request.query_params["playlist_id"]

        results = sp.playlist_tracks(playlist_id)

        return Response(results["items"])
