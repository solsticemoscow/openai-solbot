from typing import Union


import pytube


from tavily import TavilyClient

from youtubesearchpython import VideosSearch

from BOT.config import ROOT_DIR, TAVILY_API


class ClassUtils:

    def __init__(self):
        self.tavily = TavilyClient(api_key=TAVILY_API)
        self.MSGS = []

    async def get_track_id(self, file):



        shazam = Shazam(endpoint_country='US', language='en-US')

        out = await shazam.recognize_song(data=file)

        return out['track']['subtitle'] + ' - ' + out['track']['title']



    def get_redis(self):
        import redis
        from redis.commands.search.indexDefinition import (
            IndexDefinition,
            IndexType
        )
        from redis.commands.search.query import Query
        from redis.commands.search.field import (
            TextField,
            VectorField
        )

        REDIS_HOST = "localhost"
        REDIS_PORT = 6379
        REDIS_PASSWORD = ""  # default for passwordless Redis

        # Connect to Redis
        redis_client = redis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            password=REDIS_PASSWORD
        )
        redis_client.ping()




    def get_info_from_yt(self, QUERY: str = 'найди последние трэки дуа липа'):
        videosSearch = VideosSearch(query=QUERY, limit=3)

        return videosSearch.result()['result']

    def search_tavily(self, query: str = 'what is that porno?'):

        response = self.tavily.search(
            query=query,
            search_depth='advanced',
            include_images=True,
            include_answer=True,
            max_results=3
        )
        return response

    def get_content_from_youtube(self, URL: str, TYPE: str):
        try:
            YT = pytube.YouTube(url=URL)

            TRACK = YT.author + ' - ' + YT.title
            OUTPATH = '/tmp/' + TRACK

            if int(YT.length) < 600:
                if TYPE == 'yt_mp3':
                    YT.streams.get_audio_only().download(filename=TRACK + '.mp3', output_path='/tmp/')
                    return int(YT.length), OUTPATH + '.mp3'
                if TYPE == 'yt_mp4':
                    YT.streams.get_highest_resolution().download(
                        filename=TRACK + '.mp4', output_path='/tmp/')
                    return int(YT.length), OUTPATH + '.mp4'
        except Exception as e:
            return e

    def get_info_from_youtube(self, QUERY: str = 'dua lipa') -> Union[tuple, str, Exception]:
        try:
            res = pytube.Search(query=QUERY)
            VIDEO_ID = str(res.results[0]).replace('<', '').replace('>', '').rsplit(sep='videoId=')[1]
            return 'https://www.youtube.com/watch?v=' + VIDEO_ID

        except Exception as e:
            return e


UtilsClass = ClassUtils()
