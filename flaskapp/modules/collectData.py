from riotwatcher import LolWatcher, ApiError
from getKey import getKey

key = getKey()
lw = LolWatcher(key)
mr = 'kr'

"""
for get match data?

find summoner id list from LEAGUE
find account id list using summoner id from SUMMONER
find recent 20 matchlist using account id from MATCH


"""
