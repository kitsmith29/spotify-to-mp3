from requests import get
import youtube_dl

class YouTubeSearcher():

    def __init__(self):

        self.ydl_opts = {
            'format': 'bestaudio',
            'noplaylist':'True',
            }

    def searchYouTube(self, keywords : str, result_num : int) -> dict:
        
        with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
            result = ydl.extract_info(f"ytsearch{result_num}:{keywords}", download=False)['entries']
        return(result)
    
    def extractYouTubeTitles(self, result : list) -> list:
        
        title_list = []
        for vid in result:
            title = vid['title']
            title_list.append(title)
        return(title_list)    

if __name__ == "__main__":
    yt_sr = YouTubeSearcher()
    video_infos = yt_sr.searchYouTube('You and I Khruangbin', 3)
    title_list = yt_sr.extractYouTubeTitles(video_infos)
    print(title_list)