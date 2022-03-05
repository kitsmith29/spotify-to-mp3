import pandas as pd
from .connect import SpotifyConnector
from .query import SpotifyQueryHandler

class PlaylistTracks():
    
    def __init__(self, spotify_connection):
        self.sp_conn = spotify_connection
        self.sp_query = SpotifyQueryHandler()

    def getPlaylistTracks(self, playlist_id):    
        track_df = self.sp_query.extractAllQueryResults(self.sp_conn, self.sp_conn.playlist_tracks, playlist_id)
        song_df = self.sp_query.extractTrackNames(track_df)
        artist_df = self.sp_query.extractArtistNames(track_df)
        song_artist_df = pd.DataFrame({'song': song_df, 'artists': artist_df})
        return(song_artist_df)
    
class UserPlaylists():
    def __init__(self, spotify_connection):
        self.sp_conn = spotify_connection
        self.sp_query = SpotifyQueryHandler()

    def getUserPlaylistNamesIds(self, username):    
        playlist_df = self.sp_query.extractAllQueryResults(self.sp_conn, self.sp_conn.user_playlists, username)
        playlist_names = playlist_df[['name', 'id']]
        return(playlist_names)
    
if __name__ == "__main__":
    
    connector = sc.SpotifyConnector()
    sp = connector.connectToSpotify()
    up = PlaylistTracks(sp)
    tracks = up.getPlaylistTracks('5o9V8sIoMG5oKlIaUTGTs1')
    print(tracks)
    
    connector = SpotifyConnector()
    sp = connector.connectToSpotify()
    up = UserPlaylists(sp)
    playlists = up.getUserPlaylistNamesIds('joekitkat')
    print(playlists)