import youtube_dl

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

class YouTubeDownloader():
    
    def __init__(self):
        
        self.ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'logger': MyLogger(),
            'progress_hooks': [self.my_hook],
            }
        
    def my_hook(self, d : dict) -> None:
        if d['status'] == 'finished':
            print('Done downloading, now converting ...')
    
    def downloadFromURL(self, url : str) -> None:
        
        with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
            ydl.download([url])
