import nflgame
from Players import Player
from Players import WeekInfo
from Players import Stats
from Players import PassingStats
from Players import RushingStats
from Players import ReceivingStats
from Players import MiscStats


def getstats():
    years = [2016]
    weeks = [1, 2, 3]
    # weeks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    # years = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016]
    # weeks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

    yearstatline = []

    for year in years:
        print year

        for week in weeks:
            print week

            game = nflgame.games(year, week)
            players = nflgame.combine_play_stats(game)

            for p in players:
                if p.player is not None:
                    # General info
                    playerinfo = [p.player.player_id, p.player.name]

                    # Player Weekly Info
                    playerweekinfo = [p.team, p.player.position, year, week, p.home]

                    # Passing info
                    playerpassing = [p.passing_att, p.passing_cmp, p.passing_yds, p.passing_int, p.passing_tds, p.twopta, p.twoptm]

                    # Receiving info
                    playerreceiving = [p.receiving_tar, p.receiving_rec, p.receiving_yds, p.receiving_yac_yds, p.receiving_tds, p.twoptm]

                    # Rushing info
                    playerrushing = [p.rushing_att, p.rushing_yds, p.rushing_rac_yds, p.rushing_tds, p.twoptm]

                    # Misc. info
                    playermisc = [p.fumbles_tot, p.fumbles_lost]

                    weeklystatline = [playerweekinfo, playerpassing, playerreceiving, playerrushing, playermisc]
                    playerstatline = [playerinfo, weeklystatline]

                    # print playerstatline

                    yearstatline.append(playerstatline)

                else:
                    print str("Could not find info for ") + p.name

    # yearstatline.sort()

    return yearstatline


def groupstats(data):
    mergedindex = 0
    mergedlist = [data[0]]

    for statline in range(1, len(data)):
        temp = mergedlist[mergedindex][0]

        if data[statline][0] == temp:
            mergedlist[mergedindex].append(data[statline][1])
        else:
            mergedindex += 1
            mergedlist.append(data[statline])

    return mergedlist


def outputtofile(f, data):
    outputfile = open(f, 'w')

    for statline in data:
        outputfile.write("%s\n" % statline)

    return


def outputtostd(data):
    for statline in data:
        print statline

    return


def listtoobj(data):

    objlist = []

    for player in data:
        p = Player(player[0][0], player[0][1])

        for w in range(1, len(player)):
            winfo = WeekInfo(player[w][0][0], player[w][0][1], player[w][0][2], player[w][0][3], player[w][0][4])
            pstats = PassingStats(player[w][1][0], player[w][1][1], player[w][1][2], player[w][1][3], player[w][1][4], player[w][1][5], player[w][1][6])
            recstats = ReceivingStats(player[w][2][0], player[w][2][1], player[w][2][2], player[w][2][3], player[w][2][4], player[w][2][5])
            rushstats = RushingStats(player[w][3][0], player[w][3][1], player[w][3][2], player[w][3][3], player[w][3][4])
            mstats = MiscStats(player[w][4][0], player[w][4][1])

            p.addweeklystatline([winfo, pstats, recstats, rushstats, mstats])

        objlist.append(p)

    return objlist


yearStatLine = getstats()
mergedYearStatLine = groupstats(yearStatLine)

outputtofile('C:\Users\sshah\Documents\FFStats\RawData.txt', yearStatLine)
outputtofile('C:\Users\sshah\Documents\FFStats\GroupedData.txt', mergedYearStatLine)

playerObjList = listtoobj(mergedYearStatLine)

# for player in playerObjList:
#     player.printstats()

# outputtostd(mergedYearStatLine)
# print yearStatLine
# print mergedYearStatLine
# print playerObjList
