from spotify_connect import SpotifyConnector
from spotify_query import SpotifyQuery

class UserPlaylists():
    
    def __init__(self, spotify_connection):
        self.sp_conn = spotify_connection
        self.sp_query = SpotifyQuery()

    def getUserPlaylistNames(self, username):    
        playlist_df = self.sp_query.extractAllQueryResults(self.sp_conn, self.sp_conn.user_playlists, username)
        playlist_names = playlist_df['name']
        return(playlist_names)
    
if __name__ == "__main__":
    connector = SpotifyConnector()
    sp = connector.connectToSpotify()
    up = UserPlaylists(sp)
    playlist_names = up.getUserPlaylistNames('joekitkat')
    print(playlist_names)