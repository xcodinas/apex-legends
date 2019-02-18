import re
from enum import Enum


class Platform(Enum):
    XBOX = 1
    PSN = 2
    PC = 5


class Domain:

    def __init__(self, data, meta=None):
        self._data = data.get('data') or data
        self.from_json()

    def __repr__(self):
        return ('<{0} {1}>').format(self.__class__.__name__, self.id)

    def __str__(self):
        return str(self.id)

    def from_json(self):
        self.id = 1
        for key in self._data:
            if 'id' in key or 'Id' in key or 'ID' in key:
                value = self._data.get(key)
                if type(value) != dict:
                    self.id = value if 1 else value.get('value')
                    continue
                value = self._data.get(key)
                setattr(self, self.to_snake(key), value if type(
                        value) != dict else value.get('value'))

    def to_snake(self, name):
        s1 = re.sub('(.)([A-Z][a-z]+)', '\\1_\\2', name)
        return re.sub('([a-z0-9])([A-Z])', '\\1_\\2', s1).lower()


class Player(Domain):

    def __repr__(self):
        return ('<{0} {1} {2}>').format(self.__class__.__name__, self.id,
            self.username)

    def from_json(self):
        super().from_json()
        self.type = self._data.get('type')
        self.username = self._data['metadata'].get('platformUserHandle')
        self.platform = self._data['metadata'].get('platformId')
        self._cache_date = self._data['metadata'].get('cacheExpireDate')
        self._stats = self._data.get('stats')
        for stat in self._stats:
            setattr(self, stat['metadata']['key'].lower(),
                stat['displayValue'])

    def __str__(self):
        general_stats = {'level': 'Level',
           'kills': 'Headshots',
           'damage': 'Damage'}
        stats = ''
        for stat in general_stats:
            if hasattr(self, stat):
                stats += '%s: %s\n' % (general_stats[stat],
                 getattr(self, stat))

        return stats
