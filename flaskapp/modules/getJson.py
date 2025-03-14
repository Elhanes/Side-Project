import json
from riotwatcher import LolWatcher, ApiError
from getKey import getKey

src_champ = "flaskapp/static/json/champId.json"
src_item = "flaskapp/static/json/itemId.json"
src_spell = "flaskapp/static/json/spellId.json"
src_rune = "flaskapp/static/json/runeId.json"

key = getKey()
region = 'kr'
#version = lw.data_dragon.versions_for_region(region)
version = '10.16.1'

lw = LolWatcher(key)
champ_list = lw.data_dragon.champions(version)
champ = list(champ_list['data'].keys())
champ_id = {}

item_list = lw.data_dragon.items(version)
item = list(item_list['data'].keys())
item_id = {}

spell_list = lw.data_dragon.summoner_spells(version)
spell = list(spell_list['data'].keys())
spell_id = {}

rune_list = lw.data_dragon.runes_reforged(version)
rune_id = {}

for a in champ:
    champ_id[champ_list['data'][a]['key']] = a

for a in item:
    item_id[a] = item_list['data'][a]['name']

for a in spell:
    spell_id[spell_list['data'][a]['key']] = spell_list['data'][a]['name']

for rune_category in rune_list:
    rune_id[rune_category['id']] = rune_category['name']
    for rune_slot_item in rune_category['slots']:
        for rune_info in rune_slot_item['runes']:
            rune_id[rune_info['id']] = rune_info['name']

with open(src_champ, "w", encoding="utf-8") as f:
    json.dump(champ_id, f, ensure_ascii=False, indent="\t")

with open(src_item, "w", encoding="utf-8") as f:
    json.dump(item_id, f, ensure_ascii=False, indent="\t")

with open(src_spell, "w", encoding="utf-8") as f:
    json.dump(spell_id, f, ensure_ascii=False, indent="\t")

with open(src_rune, "w", encoding="utf-8") as f:
    json.dump(rune_id, f, ensure_ascii=False, indent="\t")
