from spotipy import oauth2, Spotify

class SpotifyConnector(Spotify):
    def __init__(self):
        super().__init__(Spotify)
        
        self.client_id = 'c4f8cd3d6fd243e78390e38dc1cd6767'
        self.client_secret = '86c216166e494bfaa82fb40b677f8aad'
    
    def connectToSpotify(self):
        auth_manager = oauth2.SpotifyClientCredentials(
            client_id=self.client_id,
            client_secret=self.client_secret
            )
        
        sp = Spotify(auth_manager=auth_manager)
        
        return(sp)