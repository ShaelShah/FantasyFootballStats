import nflgame
import nflgame.update_players
import pickle
import sys

from Players import Player
from Players import WeekInfo
from Players import PassingStats
from Players import RushingStats
from Players import ReceivingStats
from Players import MiscStats

# Linux files
# rawdatafile = "/home/shael/Fantasy Football Stats/RawData.txt"
# groupeddatafile = "/home/shael/Fantasy Football Stats/GroupedData.txt"
# csvfile = "/home/shael/Fantasy Football Stats/StatsCSV.csv"
# pickledatafile = "/home/shael/Fantasy Football Stats/pickle.data"

# Windows files
rawdatafile = "C:\Users\sshah\Desktop\FF\Data\\rawData.txt"
groupeddatafile = "C:\Users\sshah\Desktop\FF\Data\\groupedData.txt"
csvfile = "C:\Users\sshah\Desktop\FF\Data\\rawData.csv"
pickledatafile = "C:\Users\sshah\Desktop\FF\Data\\pickle.data"


def getstats():

    # weeks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    # years = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016]
    weeks = [1]
    years = [2017]

    yearstatline = []
    missedplayers = []

    for year in years:
        print "\nGetting data for " + str(year) + ", Weeks",

        for week in weeks:
            print week,

            game = nflgame.games(year, week)
            players = nflgame.combine_play_stats(game)

            for p in players:
                if p.player is not None:
                    if p.player.position in ('QB', 'WR', 'RB', 'TE'):
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

                        yearstatline.append(playerstatline)

                else:
                    missedplayers.append(str(year) + ', ' + str(week) + ': ' + p.name)

    if len(missedplayers) != 0:
        print "\n\nThe following players are missing information:"
        for m in missedplayers:
            print m

    yearstatline.sort()
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

    outputfile.close()

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


def outputtocsv(data):

    log = sys.stdout.write
    flush = sys.stdout.flush

    for player in data:
        p = Player(player[0][0], player[0][1])
        log('\n' + p.printcsv() + ',')

        for w in range(1, len(player)):
            winfo = WeekInfo(player[w][0][0], player[w][0][1], player[w][0][2], player[w][0][3], player[w][0][4])
            pstats = PassingStats(player[w][1][0], player[w][1][1], player[w][1][2], player[w][1][3], player[w][1][4], player[w][1][5], player[w][1][6])
            recstats = ReceivingStats(player[w][2][0], player[w][2][1], player[w][2][2], player[w][2][3], player[w][2][4], player[w][2][5])
            rushstats = RushingStats(player[w][3][0], player[w][3][1], player[w][3][2], player[w][3][3], player[w][3][4])
            mstats = MiscStats(player[w][4][0], player[w][4][1])

            log(winfo.printcsv() + ',')
            log(pstats.printcsv() + ',')
            log(recstats.printcsv() + ',')
            log(rushstats.printcsv() + ',')
            log(mstats.printcsv() + ',')

    flush


def outputtocsvfile(f, data):
    csvoutput = open(f, 'wb')

    for player in data:
        p = Player(player[0][0], player[0][1])
        csvoutput.write("\n%s," % p.printcsv())

        for w in range(1, len(player)):
            winfo = WeekInfo(player[w][0][0], player[w][0][1], player[w][0][2], player[w][0][3], player[w][0][4])
            pstats = PassingStats(player[w][1][0], player[w][1][1], player[w][1][2], player[w][1][3], player[w][1][4], player[w][1][5], player[w][1][6])
            recstats = ReceivingStats(player[w][2][0], player[w][2][1], player[w][2][2], player[w][2][3], player[w][2][4], player[w][2][5])
            rushstats = RushingStats(player[w][3][0], player[w][3][1], player[w][3][2], player[w][3][3], player[w][3][4])
            mstats = MiscStats(player[w][4][0], player[w][4][1])

            csvoutput.write("%s," % winfo.printcsv())
            csvoutput.write("%s," % pstats.printcsv())
            csvoutput.write("%s," % recstats.printcsv())
            csvoutput.write("%s," % rushstats.printcsv())
            csvoutput.write("%s," % mstats.printcsv())

    csvoutput.close()


def pickledata(f, data):
    pickleoutput = open(f, 'wb')
    pickle.dump(data, pickleoutput)
    pickleoutput.close()


def unpickledata(f):
    pickleinput = open(f, 'rb')
    return pickle.load(pickleinput)


def updatestats(updateplayers, outfile, outstd, outcsv, outputcsvfile, outpickle):
    if updateplayers:
        nflgame.update_players.run()

    yearstatline = getstats()
    mergedyearstatline = groupstats(yearstatline)

    if outfile:
        outputtofile(rawdatafile, yearstatline)
        outputtofile(groupeddatafile, mergedyearstatline)

    if outstd:
        outputtostd(yearstatline)
        outputtostd(mergedyearstatline)

    if outcsv:
        outputtocsv(mergedyearstatline)

    if outputcsvfile:
        outputtocsvfile(csvfile, mergedyearstatline)

    playerobjlist = listtoobj(mergedyearstatline)

    if outpickle:
        pickledata(pickledatafile, playerobjlist)

    return playerobjlist


def getpickledata():
    return unpickledata(pickledatafile)


updatestats(0, 0, 0, 0, 1, 0)


