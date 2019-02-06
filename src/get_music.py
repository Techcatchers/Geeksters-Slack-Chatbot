import pafy
import requests
from bs4 import BeautifulSoup
try:
    import bitly_api
except ModuleNotFoundError:
    raise ModuleNotFoundError("Please read this article to install Bitly_api: https://www.geeksforgeeks.org/python-how-to-shorten-long-urls-using-bitly-api/")
import settings


def music(song_name):
    """
        Takes song_name as an argument.
        Formats the song name and passes it to Youtube Data API.
        It then extracts teh video id and title from the first Youtube result.
        The video is converted into an Audio with Medium Bitrate settings.
        Audio and Video is formatted and shortened using Bitly API.
        Returns title, audio link and video link as a tuple.
    """

    API_USER = settings.BITLY_API_USER
    API_KEY = settings.BITLY_API_KEY

    b = bitly_api.Connection(API_USER, API_KEY)

    song_name = song_name + " song"

    url = "https://www.googleapis.com/youtube/v3/search?part=snippet&q=" + song_name + \
        "&key=" + settings.YTDATA_API_KEY + "&maxResults=1&type=video"
    page = requests.get(url)
    data = page.json()
    sear = data["items"][0]["id"]["videoId"]
    title = data["items"][0]["snippet"]["title"]

    myaud = pafy.new(sear)
    genlink = myaud.audiostreams[2].url
    vlink = "https://www.youtube.com/watch?v=" + sear

    flink = b.shorten(uri=genlink)
    flink = flink["url"]
    vlink = b.shorten(uri=vlink)
    vlink = vlink["url"]

    return (title, flink, vlink)


# print(music("tere sang yaara"))
