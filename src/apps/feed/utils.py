import feedparser
import re

# CONSTANTS
CNN, TEMPO, JAWA_POST, KUMPARAN = 'cnn', 'tempo', 'jawa_pos', 'kumparan'

NEWS_CHANNELS = {
    CNN: 'CNN',
    TEMPO: 'Tempo',
    JAWA_POST: 'Jawa Post',
    KUMPARAN: 'Kumparan',
}

RSS_NEWS_FEEDS = {
    CNN: 'https://www.cnnindonesia.com/nasional/rss',
    TEMPO: 'http://rss.tempo.co/nasional',
    JAWA_POST: 'https://www.jawapos.com/nasional/rss',
    KUMPARAN: 'https://lapi.kumparan.com/v2.0/rss/'
}


# functions
def is_news_supported(news) -> object:
    """ check if news channel supported or not """
    return news in NEWS_CHANNELS.keys()


def get_articles(channel):
    feed_parse = feedparser.parse(RSS_NEWS_FEEDS.get(channel))
    return feed_parse.get('entries', [])


def clean_html(text: str) -> str:
    """ remove html tag from string """
    return re.sub(re.compile('<.*?>'), '', text)
