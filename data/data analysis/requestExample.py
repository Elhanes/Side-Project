from riotwatcher import LolWatcher, ApiError
import pandas as pd

api_key = "RGAPI-e8c6a8e0-30ad-4185-9456-9fb25de6358d"
watcher = LolWatcher(api_key)
region = 'kr'

me = watcher.summoner.by_name(region, "개산벽")
rank = watcher.league.by_summoner(region, me['id'])
match = watcher.match.matchlist_by_account(region, me['accountId'])
last_match = match['matches'][0]
detail = watcher.match.by_id(region, last_match['gameId'])

participants = []

for row in detail['participants']:
    participants_row = {}
    participants_row['champion'] = row['championId']
    participants_row['spell1'] = row['spell1Id']
    participants_row['spell2'] = row['spell2Id']
    participants_row['win'] = row['stats']['win']
    participants_row['kills'] = row['stats']['kills']
    participants_row['deaths'] = row['stats']['deaths']
    participants_row['assists'] = row['stats']['assists']
    participants_row['totalDamageDealt'] = row['stats']['totalDamageDealt']
    participants_row['goldEarned'] = row['stats']['goldEarned']
    participants_row['champLevel'] = row['stats']['champLevel']
    participants_row['totalMinionsKilled'] = row['stats']['totalMinionsKilled']
    participants_row['item0'] = row['stats']['item0']
    participants_row['item1'] = row['stats']['item1']
    participants.append(participants_row)

df = pd.DataFrame(participants)
#df

print(df)

df.to_excel('example.xlsx', sheet_name='sheet1')