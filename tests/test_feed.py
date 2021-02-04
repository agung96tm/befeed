from .base import client
from apps.feed import (
    CNN,
    is_news_supported
)


def test_returns_true_when_channel_exist(client):
    assert is_news_supported(CNN) is True


def test_returns_false_when_channel_doesnt_exist(client):
    assert is_news_supported('wrong') is False
