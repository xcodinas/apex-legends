import json
import pytest
import requests_mock
from furl import furl
from unittest.mock import Mock, patch

from apex_legends import ApexLegends
from apex_legends.base import Client
from apex_legends.domain import Platform, Player


api = ApexLegends('apikey')
BASE_URL = Client.BASE_URL


@pytest.fixture()
def mock():
    with requests_mock.Mocker() as mock:
        yield mock


@pytest.fixture()
def player_response():
    with open('tests/player_response.json') as json_file:
        yield json.load(json_file)


@pytest.fixture()
def player_sessions_response():
    with open('tests/player_sessions_response.json') as json_file:
        yield json.load(json_file)


def test_player_get(mock, player_response, player_sessions_response):
    player_id = 'Player'
    player_url = furl(BASE_URL).join('profile/%s/%s' % (
            Platform.PC.value, player_id)).url
    sessions_url = player_url + '/sessions'
    mock.register_uri('GET', player_url, json=player_response)
    mock.register_uri('GET', sessions_url, json=player_sessions_response)
    player = api.player(player_name=player_id, platform=Platform.PC)
    assert isinstance(player, Player)
    assert player.username == player_id
    assert player.sessions
