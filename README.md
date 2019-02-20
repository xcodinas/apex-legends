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

