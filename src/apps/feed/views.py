from flask import render_template, abort, request

from . import feed
from .utils import NEWS_CHANNELS, CNN, is_news_supported, get_articles


@feed.route('/')
def home():
    return render_template('home.html')


@feed.route('/<news_name>')
def news_channel(news_name):
    if not is_news_supported(news_name):
        abort(404)
    return render_template('news.html',
                           display_name=NEWS_CHANNELS[news_name],
                           articles=get_articles(news_name))


@feed.route('/search')
def search():
    news_name = request.args.get('publication', '').lower()
    news_name = CNN if news_name == '' else news_name

    if not is_news_supported(news_name):
        abort(404)

    return render_template(
        'news.html',
        search_publication=news_name,
        display_name=NEWS_CHANNELS.get(news_name, 'Empty'),
        articles=get_articles(news_name)
    )
