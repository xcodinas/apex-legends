[![PyPI version](https://badge.fury.io/py/apex-legends.svg)](https://badge.fury.io/py/apex-legends)

# apex-legends
Python wrapper for https://apex.tracker.gg/ api.

## Installation

You can install it via setup.py

```
python setup.py install
```

or from pip:

```
pip install apex-legends
```


## Usage

You need to register for an api key at https://apex.tracker.gg/

Then it's just easy as:

```
from apex_legends import ApexLegends

apex = ApexLegends("apex_api_key")

player = apex.player('NRG_dizzy')

print(player)

for legend in player.legends:
    print(legend.legend_name)
    print(legend.icon)
    print(legend.damage)
```

## Asynchronous Calls

For those who wish to use this API wrapper for their asynchronous applications, you may do so by calling the `AsyncLegends` class.

**WARNING**: This portion of the wrapper is for use with Python version 3.5+. [PEP 492](https://www.python.org/dev/peps/pep-0492/) released the keywords `async` and `await`,  as well as the magic methods `__aenter__` and `__aexit__`, which this portion of the wrapper takes advantage of. This results in the asynchronous class not being compatible with Python versions 3.4 and lower.

```py
import asyncio

from apex_legends import AsyncLegends
from apex_legends.domain import Platform

my_api_key = 'https://apex.tracker.gg api key here'


async def main(api_key, player_name, platform=None):
    async with AsyncLegends(api_key) as apex:
        player = await apex.player(player_name, platform=platform if platform else Platform.PC)
    return player

loop = asyncio.get_event_loop()
result = loop.run_until_complete(main(my_api_key, player_name='NRG_dizzy'))

print(result)

for legend in result.legends:
    print(legend.legend_name)
    print(legend.icon)
    print(getattr(legend, 'damage', 'Damage not found.'))
```
