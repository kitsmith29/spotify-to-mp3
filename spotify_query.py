import pandas as pd
from spotify_connect import SpotifyConnector

class SpotifyQuery():
    
    def extractAllQueryResults(self, sp_conn, sp_func, params=None):
        results = sp_func(params)
        total_results = results['items']
        while results['next']:
            results = sp_conn.next(results)
            total_results.extend(results['items'])
        total_df = pd.DataFrame(total_results)
        return(total_df)