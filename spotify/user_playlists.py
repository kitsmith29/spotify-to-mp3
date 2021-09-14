from spotify_connect import SpotifyConnector
from spotify_query import SpotifyQueryHandler

class UserPlaylists():
    
    def __init__(self, spotify_connection):
        self.sp_conn = spotify_connection
        self.sp_query = SpotifyQueryHandler()

    def getUserPlaylistNamesIds(self, username):    
        playlist_df = self.sp_query.extractAllQueryResults(self.sp_conn, self.sp_conn.user_playlists, username)
        playlist_names = playlist_df[['name', 'id']]
        return(playlist_names)
          
if __name__ == "__main__":
    connector = SpotifyConnector()
    sp = connector.connectToSpotify()
    up = UserPlaylists(sp)
    playlists = up.getUserPlaylistNamesIds('joekitkat')
    print(playlists)