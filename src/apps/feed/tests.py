from unittest.mock import patch

from flask import url_for

from apps.feed.utils import NEWS_CHANNELS, is_news_supported, CNN
from core.test.base import BaseTest


class HomeViewTest(BaseTest):
    def test_passes_home_page(self):
        response = self.client.get(url_for('feed.home'))
        self.assertTrue('News Channels' in response.get_data(as_text=True))

    def test_success_go_to_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_success_home_page_show_all_of_news_channels(self):
        response = self.client.get('/')
        response = response.data.decode("utf-8")

        for name, display_name in NEWS_CHANNELS.items():
            with self.subTest('test channel is exist', channel=name):
                self.assertIn(display_name, response)


@patch('apps.feed.views.get_articles', return_values=[])
class NewsChannelTest(BaseTest):
    def test_success_go_to_news_channel_page(self, mock_get_articles):
        channels = list(NEWS_CHANNELS.keys())
        response = self.client.get(f'/{channels[0]}')
        self.assertEqual(response.status_code, 200)

    def test_fail_404_when_channel_doesnt_exist(self, mock_get_articles):
        response = self.client.get(f'/wrong_channel')
        self.assertEqual(response.status_code, 404)


@patch('apps.feed.views.get_articles', return_values=[])
class SearchViewTest(BaseTest):
    def test_success_go_to_search_page(self, mock_get_articles):
        response = self.client.get(f'/search')
        self.assertEqual(response.status_code, 200)


class UtilTest(BaseTest):
    def test_returns_boolean_to_check_condition_of_news_is_exist_or_not(self):
        news_channels = {
            CNN: True, 'Wrong': False
        }
        for news, condition in news_channels.items():
            with self.subTest('test news is exist', news=news):
                is_exist = is_news_supported(news)
                self.assertEqual(is_exist, condition)
