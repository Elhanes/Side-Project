from riotwatcher import LolWatcher, ApiError

key = '1'
region = 'kr'

lw = LolWatcher(key)
#version = lw.data_dragon.versions_for_region(region)
champ_list = lw.data_dragon.champions('10.16.1')
champ = list(champ_list['data'].keys())
champId = {}

for a in champ:
    champId[champ_list['data'][a]['key']] = a

print(champId)
