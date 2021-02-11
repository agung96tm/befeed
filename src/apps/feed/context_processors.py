from . import feed
from .utils import NEWS_CHANNELS, clean_html


@feed.context_processor
def utility_processor():
    return dict(news_channels=NEWS_CHANNELS, clean_html=clean_html)
