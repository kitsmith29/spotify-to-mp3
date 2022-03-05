from decouple import config
from spotipy import oauth2, Spotify


class SpotifyConnector(Spotify):
    def __init__(self):
        super().__init__(Spotify)

        self.client_id = config["CLIENT_ID"]
        self.client_secret = config["CLIENT_SECRET"]

    def connectToSpotify(self):
        auth_manager = oauth2.SpotifyClientCredentials(
            client_id=self.client_id, client_secret=self.client_secret
        )

        sp = Spotify(auth_manager=auth_manager)

        return sp
