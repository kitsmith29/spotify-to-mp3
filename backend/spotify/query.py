import pandas as pd

class SpotifyQueryHandler():
    
    def extractAllQueryResults(self, sp_conn, sp_func, params=None):
        results = sp_func(params)
        total_results = results['items']
        while results['next']:
            results = sp_conn.next(results)
            total_results.extend(results['items'])
        total_df = pd.DataFrame(total_results)
        return(total_df)
    
    def extractTrackNames(self, track_df):
        track_df = track_df['track'].apply(lambda x: x.get('name'))
        return(track_df)
        
    def extractArtistNames(self, track_df):
        artist_df = track_df['track'].apply(lambda x: x.get('artists'))
        def retrieve_artists(x):
            artist_list = []
            num_of_artists = len(x)
            for n in range(0, num_of_artists):
                artist_list.append("%s" %(x[n].get('name')))
            return(artist_list)
        artist_df = artist_df.apply(lambda x: retrieve_artists(x))
        return(artist_df)