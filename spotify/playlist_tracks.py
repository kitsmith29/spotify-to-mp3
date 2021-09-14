import pandas as pd
from spotify import spotify_connect as sc
from spotify import spotify_query as sq

class PlaylistTracks():
    
    def __init__(self, spotify_connection):
        self.sp_conn = spotify_connection
        self.sp_query = sq.SpotifyQueryHandler()

    def getPlaylistTracks(self, playlist_id):    
        track_df = self.sp_query.extractAllQueryResults(self.sp_conn, self.sp_conn.playlist_tracks, playlist_id)
        song_df = self.sp_query.extractTrackNames(track_df)
        artist_df = self.sp_query.extractArtistNames(track_df)
        song_artist_df = pd.DataFrame({'song': song_df, 'artists': artist_df})
        return(song_artist_df)
    
if __name__ == "__main__":
    
    connector = sc.SpotifyConnector()
    sp = connector.connectToSpotify()
    up = PlaylistTracks(sp)
    tracks = up.getPlaylistTracks('5o9V8sIoMG5oKlIaUTGTs1')
    print(tracks)