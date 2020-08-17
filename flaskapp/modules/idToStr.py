import json


def champIdtoStr(id):
    with open("flaskapp/static/json/champId.json", "r", encoding="utf-8") as f:
        champ_json = json.load(f)

    return champ_json[str(id)]


def spellIdtoStr(id):
    with open("flaskapp/static/json/spellId.json", "r", encoding="utf-8") as f:
        spell_json = json.load(f)

    return spell_json[str(id)]


def itemIdtoStr(id):
    if id == 0:
        return "None"
    else:
        with open("flaskapp/static/json/itemId.json", "r", encoding="utf-8") as f:
            item_json = json.load(f)
        return item_json[str(id)]


def runeIdtoStr(id):
    with open("flaskapp/static/json/runeId.json", "r", encoding="utf-8") as f:
        rune_json = json.load(f)

    return rune_json[str(id)]
