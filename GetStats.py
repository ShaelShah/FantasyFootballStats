import nflgame
import sys


def getstats(sort):
    # years = [2016]
    # weeks = [1, 2, 3]
    years = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016]
    weeks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

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

                    weeklystatline = []

                    # Player Weekly Info
                    playerweekinfo = [p.team, p.player.position, year, week, p.home]

                    # Passing info
                    playerpassing = [p.passing_att, p.passing_cmp, p.passing_yds, p.passing_int, p.passing_tds,
                                     p.twopta, p.twoptm]

                    # Receiving info
                    playerreceiving = [p.receiving_tar, p.receiving_rec, p.receiving_yds, p.receiving_yac_yds,
                                       p.receiving_tds, p.twoptm]

                    # Rushing info
                    playerrushing = [p.rushing_att, p.rushing_yds, p.rushing_rac_yds, p.rushing_tds, p.twoptm]

                    # Misc. info
                    playermisc = [p.fumbles_tot, p.fumbles_lost]

                    weeklystatline.append([playerweekinfo, playerpassing, playerreceiving, playerrushing, playermisc])
                    playerstatline = [playerinfo, weeklystatline]
                    yearstatline.append(playerstatline)

                else:
                    print str("Could not find info for ") + p.name

    if sort:
        yearstatline.sort()

    return yearstatline


def groupstats(yearstatline):
    mergedindex = 0
    mergedlist = [yearstatline[0]]

    for statline in range(1, len(yearstatline)):
        temp = mergedlist[mergedindex][0]

        if yearstatline[statline][0] == temp:
            mergedlist[mergedindex].extend(yearstatline[statline][1])
        else:
            mergedindex += 1
            mergedlist.append(yearstatline[statline])

    return mergedlist


def outputtofile(file, data):
    f = open(file, 'w')

    for statline in data:
        f.write("%s\n" % statline)

    return


def outputtostd(data):
    for statline in data:
        print statline

    return

yearStatLine = getstats(True)
mergedYearStatLine = groupstats(yearStatLine)

outputtofile('C:\Users\sshah\Documents\FFStats\RawData.txt', yearStatLine)
outputtofile('C:\Users\sshah\Documents\FFStats\GroupedData.txt', mergedYearStatLine)

outputtostd(mergedYearStatLine)
