from .base import client
from apps.feed import NEWS_CHANNELS


# ---
# Home
# ---
def test_success_go_to_home_page(client):
    response = client.get('/')
    assert response.status_code == 200


def test_success_home_page_show_all_of_news_channels(client):
    response = client.get('/')
    response = response.data.decode("utf-8")

    for name, display_name in NEWS_CHANNELS.items():
        assert f'{display_name}' in response


# ---
# Channel
# ---
def test_success_go_to_news_channel_page(client):
    channels = list(NEWS_CHANNELS.keys())
    response = client.get(f'/{channels[0]}')
    assert response.status_code == 200


def test_fail_404_when_channel_doesnt_exist(client):
    channel = 'wrong'
    response = client.get(f'/{channel}')
    assert response.status_code == 404
