from flask import Flask, render_template

from apps.feed import NEWS_CHANNELS, is_news_supported, get_articles
from utils import clean_html, http_404

app = Flask(__name__)


# context_processors
@app.context_processor
def utility_processor():
    return dict(news_channels=NEWS_CHANNELS, clean_html=clean_html)


# routers
@app.route('/')
def home():
    return render_template('home.html', news_channels=NEWS_CHANNELS)


@app.route('/<news_name>')
def news_channel(news_name):
    if not is_news_supported(news_name):
        return http_404('Channel is not supported')
    return render_template('news.html',
                           display_name=NEWS_CHANNELS[news_name],
                           articles=get_articles(news_name))


if __name__ == '__main__':
    app.run()
