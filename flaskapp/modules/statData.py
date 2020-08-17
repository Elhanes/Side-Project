from riotwatcher import LolWatcher, ApiError
from flaskapp.modules.idToStr import *
from datetime import datetime

"""
for get stat data?

find account id and summoner id from SUMMONER
find lank info using summoner id from league
find recent 20 matchlist using account id from MATCH
find each match infomation using match id from MATCH

what should I consider for summarize each match?

get game mode, date, win or lose
get user`s kda, champ, item.
get other players name, champ.

"""


def statSearch(key, region, value):
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
        rankList = [0] * len(leagueInfo)
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

    match = lw.match.by_id(region, '4581401986')

    for match_user_info in match['participantIdentities']:
        if match_user_info['player']['summonerName'] == value:
            match_user_id = match_user_info['participantId']
            break

    match_test = {}
    match_test['time'] = datetime.fromtimestamp(match['gameCreation']/1000)
    match_test['duration'] = match['gameDuration'] / 60
    match_test['mode'] = match['gameMode']
    match_test['champ'] = champIdtoStr(
        match['participants'][match_user_id - 1]["championId"])
    match_test['spell1'] = spellIdtoStr(
        match['participants'][match_user_id - 1]["spell1Id"])
    match_test['spell2'] = spellIdtoStr(
        match['participants'][match_user_id - 1]["spell2Id"])
    match_test['item0'] = itemIdtoStr(match['participants'][match_user_id -
                                                            1]["stats"]["item0"])
    match_test['item1'] = itemIdtoStr(match['participants'][match_user_id -
                                                            1]["stats"]["item1"])
    match_test['item2'] = itemIdtoStr(match['participants'][match_user_id -
                                                            1]["stats"]["item2"])
    match_test['item3'] = itemIdtoStr(match['participants'][match_user_id -
                                                            1]["stats"]["item3"])
    match_test['item4'] = itemIdtoStr(match['participants'][match_user_id -
                                                            1]["stats"]["item4"])
    match_test['item5'] = itemIdtoStr(match['participants'][match_user_id -
                                                            1]["stats"]["item5"])
    match_test['item6'] = itemIdtoStr(match['participants'][match_user_id -
                                                            1]["stats"]["item6"])
    match_test['kill'] = match['participants'][match_user_id -
                                               1]["stats"]["kills"]
    match_test['death'] = match['participants'][match_user_id -
                                                1]["stats"]["deaths"]
    match_test['assist'] = match['participants'][match_user_id -
                                                 1]["stats"]["assists"]
    match_test['champLevel'] = match['participants'][match_user_id -
                                                     1]["stats"]["champLevel"]
    match_test['runeMain'] = runeIdtoStr(match['participants'][match_user_id -
                                                               1]["stats"]["perkPrimaryStyle"])
    match_test['runeSub'] = runeIdtoStr(match['participants'][match_user_id -
                                                              1]["stats"]["perkSubStyle"])
    match_test['runeCore'] = runeIdtoStr(match['participants'][match_user_id -
                                                               1]["stats"]["perk0"])

    stat['match'] = match_test
    return stat
