# apex-legends
Python wrapper for https://apex.tracker.gg/ api.

## Installation

You can install it via setup.py

```
python setup.py install
```


## Usage

You need to register for an api key at https://apex.tracker.gg/

Then it's just easy as:

```
from apex_legends import ApexLegends

apex = ApexLegends("apex_api_key")

player = apex.player('NRG_dizzy')

print(player)
```
