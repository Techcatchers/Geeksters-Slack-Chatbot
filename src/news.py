try:
    import bitly_api
except ModuleNotFoundError:
    raise ModuleNotFoundError("Please read this article to install Bitly_api: https://www.geeksforgeeks.org/python-how-to-shorten-long-urls-using-bitly-api/")
import requests
import settings

def get_news():
    """
        Fetches latest news from News API.
        Collects the top 5 news from google news.
        Shortens news links using Bitly APIs.
        Returns Aggregated news.
    """

    API_USER = settings.BITLY_API_USER
    API_KEY = settings.BITLY_API_KEY

    bitly_conn = bitly_api.Connection(API_USER, API_KEY)
    url = "https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=" + settings.NEWS_API_KEY

    news = requests.get(url)
    data = news.json()

    get_news = ''
    for i in range(5):
        title = data["articles"][i]["title"]
        description = data["articles"][i]["description"]
        link = data["articles"][i]["url"]
        flink = bitly_conn.shorten(uri=link)
        flink = flink["url"]
        get_news += "*" + title + " :* _" + description + "_ \n" + flink + "\n\n"

    return get_news

# print(news())