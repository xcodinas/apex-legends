import json

import furl
import requests
import aiohttp

from .exceptions import (UnauthorizedError, NotFoundError, UnknownPlayerError,
    ServerError)
from .domain import Platform, Player


class ApexLegends:

    def __init__(self, api_key):
        self.client = Client(api_key)

    def player(self, player_name=None, platform=Platform.PC):
        endpoint = 'profile/%s/%s' % (platform.value, player_name)
        data = self.client.request(endpoint)

        # Load the game session data
        games_endpoint = endpoint + '/sessions'
        sessions = self.client.request(games_endpoint)
        if data.get('data') and 'userInfo' in data.get('data'):
            player = Player(data)
            player.set_sessions(session_data=sessions.get('data'))
            return player
        raise UnknownPlayerError


class AsyncLegends:

    def __init__(self, api_key):
        self.client = AsyncClient(api_key)

    async def __aenter__(self):
        return self

    async def __aexit__(self, *a):
        pass

    async def player(self, player=None, platform=Platform.PC):
        endpoint = 'profile/%s/%s' % (platform.value, player)
        data = await self.client.request(endpoint)
        if data.get('data') and 'id' in data.get('data'):
            return Player(data)
        raise UnknownPlayerError


class Client:
    BASE_URL = 'https://public-api.tracker.gg/v2/apex/standard/'

    def __init__(self, api_key):
        self.session = requests.Session()
        self.session.headers.update({'TRN-Api-Key': api_key,
                                     'Accept': 'application/vnd.api+json'})
        self.url = furl.furl(self.BASE_URL)

    API_OK = 200
    API_ERRORS_MAPPING = {
        401: UnauthorizedError,
        400: NotFoundError,
        403: UnauthorizedError,
        404: UnknownPlayerError,
        500: ServerError,
    }

    def request(self, endpoint):
        response = self.session.get(self.BASE_URL + endpoint)
        if response.status_code != self.API_OK:
            exception = self.API_ERRORS_MAPPING.get(
                response.status_code, Exception)
            raise exception
        return json.loads(response.text)


class AsyncClient(Client):

    def __init__(self, api_key):
        self.headers = {'TRN-Api-Key': api_key,
            'Accept': 'application/vnd.api+json'}
        self._session = aiohttp.ClientSession(headers=self.headers)

    async def __aenter__(self):
        if not self._session:
            self._session = aiohttp.ClientSession(headers=self.headers)

    async def __aexit__(self, *a):
        await self._session.close()

    async def request(self, endpoint):
        async with self._session.get(self.BASE_URL + endpoint) as response:
            if not response.status == self.API_OK:
                exception = self.API_ERRORS_MAPPING.get(response.status,
                    Exception)
                raise exception
            await self._session.close()
            return await response.json()
