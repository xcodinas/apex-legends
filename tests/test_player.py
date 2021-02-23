from apex_legends import ApexLegends
from apex_legends.domain import Platform

API_KEY = "Tracker API Key Here"


def test_player():
    apex = ApexLegends(API_KEY)
    player = apex.player(player='GoshDarnedHero', platform=Platform.PC)
    assert player.username == 'GoshDarnedHero'
    # values below should be adjusted for different users, but we'll use mine here since I know the values
    assert len(player.legends) > 1
    assert int(player.kills) >= 25
    assert int(player.matchesplayed) >= 189
    assert float(player.killspermatch) == round(int(player.kills) / int(player.matchesplayed), 2)
    assert int(player.damage) >= 12638
    assert player.damagepermatch == round(player.damage / player.matchesplayed, 2)
