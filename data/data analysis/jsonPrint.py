import json

version = "10.15.1"
json_src = "../dragontail/dragontail-" + version + "/" + version + "/data/en_US/champion/Aatrox.json"

with open(json_src, "r", encoding="utf-8") as f:
    champInfo = json.load(f)

print(json.dumps(champInfo, indent="\t")) #for json file text