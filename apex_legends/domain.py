import re
from enum import Enum


class Platform(Enum):
    XBOX = "xbl"
    PSN = "psn"
    PC = "origin"


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
        self.username = self._data['platformInfo'].get('platformUserHandle')
        self.platform = self._data['platformInfo'].get('platformSlug')
        assert self._data['segments'][0].get('type') == 'overview'
        self._stats = self._data['segments'][0]['stats']
        for stat, value in self._stats.items():
            setattr(self, stat.lower(),
                value['value'])
        self.legends = []
        for segment in self._data.get('segments'):
            if segment['type'] == 'legend':
                self.legends.append(Legend(segment))

    def set_sessions(self, session_data):
        self.sessions = []
        for data in session_data['items']:
            self.sessions.append(Session(data))

    def __str__(self):
        general_stats = {'level': 'Level',
           'kills': 'Total kills',
           'damage': 'Damage'}
        stats = ''
        for stat in general_stats:
            if hasattr(self, stat):
                stats += '%s: %s\n' % (general_stats[stat],
                 getattr(self, stat))

        return stats


class Legend(Domain):

    def from_json(self):
        super().from_json()
        self._stats = self._data.get('stats')
        self.legend_name = self._data['metadata'].get('name')
        self.icon = self._data['metadata'].get('imageUrl')
        self.bgimage = self._data['metadata'].get('bgImageUrl')
        for stat, value in self._stats.items():
            setattr(self, stat.lower(),
                    value['value'])


class Session(Domain):

    def from_json(self):
        super().from_json()
        self._stats = self._data.get('stats')
        for stat, value in self._stats.items():
            setattr(self, stat.lower(),
                    value['value'])
