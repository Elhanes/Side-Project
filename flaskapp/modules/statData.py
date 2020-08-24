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
    account_id = summoner['accountId']
    summoner_id = summoner['id']
    league_info = lw.league.by_summoner(region, summoner_id)  # request 2
    match_info = lw.match.matchlist_by_account(
        region, account_id, None, None, None, 0, 9)  # request 3

    # summoner information
    stat['nickname'] = value
    stat['icon'] = summoner['profileIconId']
    stat['level'] = summoner['summonerLevel']

    # rank information
    if len(league_info) == 0:
        stat['league'] = 'unranked'
    else:
        rank_list = [0] * len(league_info)
        for i in range(0, len(league_info)):
            rank_info = {}
            rank_info['queue'] = league_info[i]['queueType']
            rank_info['tier'] = league_info[i]['tier']
            rank_info['rank'] = league_info[i]['rank']
            rank_info['point'] = league_info[i]['leaguePoints']
            rank_info['win'] = league_info[i]['wins']
            rank_info['lose'] = league_info[i]['losses']
            rank_info['rate'] = round(
                rank_info['win']/(rank_info['win']+rank_info['lose'])*100, 2)
            rank_list[i] = rank_info
        stat['league'] = rank_list

    # match information
    match_user_id = 0
    match_list = []

    for match_data in match_info['matches']:
        match = lw.match.by_id(region, match_data['gameId'])  # request 4~23
        for match_user_info in match['participantIdentities']:
            if match_user_info['player']['summonerName'] == value:
                match_user_id = match_user_info['participantId']
                break

        tmp_match = {}
        tmp_match['time'] = datetime.fromtimestamp(
            match['gameCreation']/1000)
        tmp_match['duration'] = match['gameDuration'] / 60
        tmp_match['mode'] = match['gameMode']
        tmp_match['champ'] = champIdtoStr(
            match['participants'][match_user_id - 1]["championId"])
        tmp_match['spell1'] = spellIdtoStr(
            match['participants'][match_user_id - 1]["spell1Id"])
        tmp_match['spell2'] = spellIdtoStr(
            match['participants'][match_user_id - 1]["spell2Id"])
        tmp_match['item0'] = itemIdtoStr(match['participants'][match_user_id -
                                                               1]["stats"]["item0"])
        tmp_match['item1'] = itemIdtoStr(match['participants'][match_user_id -
                                                               1]["stats"]["item1"])
        tmp_match['item2'] = itemIdtoStr(match['participants'][match_user_id -
                                                               1]["stats"]["item2"])
        tmp_match['item3'] = itemIdtoStr(match['participants'][match_user_id -
                                                               1]["stats"]["item3"])
        tmp_match['item4'] = itemIdtoStr(match['participants'][match_user_id -
                                                               1]["stats"]["item4"])
        tmp_match['item5'] = itemIdtoStr(match['participants'][match_user_id -
                                                               1]["stats"]["item5"])
        tmp_match['item6'] = itemIdtoStr(match['participants'][match_user_id -
                                                               1]["stats"]["item6"])
        tmp_match['kill'] = match['participants'][match_user_id -
                                                  1]["stats"]["kills"]
        tmp_match['death'] = match['participants'][match_user_id -
                                                   1]["stats"]["deaths"]
        tmp_match['assist'] = match['participants'][match_user_id -
                                                    1]["stats"]["assists"]
        tmp_match['champLevel'] = match['participants'][match_user_id -
                                                        1]["stats"]["champLevel"]
        tmp_match['runeMain'] = runeIdtoStr(match['participants'][match_user_id -
                                                                  1]["stats"]["perkPrimaryStyle"])
        tmp_match['runeSub'] = runeIdtoStr(match['participants'][match_user_id -
                                                                 1]["stats"]["perkSubStyle"])
        tmp_match['runeCore'] = runeIdtoStr(match['participants'][match_user_id -
                                                                  1]["stats"]["perk0"])
        match_list.append(tmp_match)

    stat['match'] = match_list
    return stat
