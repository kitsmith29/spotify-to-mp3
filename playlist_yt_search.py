import pandas as pd
from spotify_connect import SpotifyConnector
from playlist_tracks import PlaylistTracks
from youtube_search import YouTubeSearcher

class PlaylistYTSearcher():
    
    def __init__(self):
        
        connector = SpotifyConnector()
        self.sp = connector.connectToSpotify()
        
    def generateSearchStringDFColumn(self, df):
        
        def extract_artists(artist_list):
            artist_str = " "
            for artist in artist_list:
                artist_str += artist
            return(artist_str)
        
        df['artist search'] = df['artist'].apply(lambda x: extract_artists(x))
        
        df['yt search'] = df['song'] + df ['artist search']
        
        print(df['yt search'])
        return(df['yt search'])
    
    def getTopThreeYTResults(self, playlist_id):
        
        title_df = pd.DataFrame(columns = ['yt_titles'])
        
        pl_tr = PlaylistTracks(self.sp)
        song_artist_df = pl_tr.getPlaylistTracks(playlist_id)
        yt_search_df = self.generateSearchStringDFColumn(song_artist_df)
        
        yt_sr = YouTubeSearcher()
        for search in yt_search_df:
            result = yt_sr.searchYouTube(search, 3)
            title_list = yt_sr.extractYouTubeTitles(result)
            title_df.append([title_list])
            
        return(results_df)
        
if __name__ == "__main__":
    pl_sr = PlaylistYTSearcher()
    results_df = pl_sr.getTopThreeYTResults('5o9V8sIoMG5oKlIaUTGTs1')
    print(results_df)