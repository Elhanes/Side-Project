from riotwatcher import LolWatcher, ApiError

key = '1'
value = '개산벽'
region = 'kr'

lw = LolWatcher(key)
stat = {}
summoner = lw.summoner.by_name(region, value)  # request 1
accountId = summoner['accountId']
summonerId = summoner['id']
leagueInfo = lw.league.by_summoner(region, summonerId)  # request 2
matchInfo = lw.match.matchlist_by_account(
    region, accountId, None, None, None, 0, 20)  # request 3

stat['nickname'] = value
stat['icon'] = summoner['profileIconId']
stat['level'] = summoner['summonerLevel']

if len(leagueInfo) == 0:
    stat['league'] = 'unranked'

else:
    rankList = [0 for _ in range(len(leagueInfo))]
    for i in range(0, len(leagueInfo)):
        rankInfo = {}
        rankInfo['queue'] = leagueInfo[i]['queueType']
        rankInfo['tier'] = leagueInfo[i]['tier']
        rankInfo['rank'] = leagueInfo[i]['rank']
        rankInfo['point'] = leagueInfo[i]['leaguePoints']
        rankInfo['win'] = leagueInfo[i]['wins']
        rankInfo['lose'] = leagueInfo[i]['losses']
        rankInfo['rate'] = round(
            rankInfo['win']/(rankInfo['win']+rankInfo['lose'])*100, 2)
        rankList[i] = rankInfo
    stat['league'] = rankList

matchList = [0 for _ in range(len(matchInfo['matches']))]
