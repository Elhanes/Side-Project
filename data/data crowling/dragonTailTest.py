from riotwatcher import LolWatcher, ApiError
import json
from ...flaskapp.modules.getKey import getKey

key = getKey()
region = 'kr'
#version = lw.data_dragon.versions_for_region(region)
version = '10.16.1'

lw = LolWatcher(key)

rune_list = lw.data_dragon.runes_reforged(version)
spell_list = lw.data_dragon.summoner_spells(version)

with open("rune_test.json", "w", encoding="utf-8") as f:
    json.dump(rune_list, f, ensure_ascii=False, indent="\t")

"""
with open("spell_test.json", "w", encoding="utf-8") as f:
    json.dump(spell_list, f, ensure_ascii=False, indent="\t")
"""
