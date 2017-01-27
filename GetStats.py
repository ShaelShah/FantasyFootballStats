import nflgame
import xml.etree.cElementTree as ET

weeks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
yearStatLine = []

for week in weeks:

    print week

    game = nflgame.games(2016, week)
    players = nflgame.combine_play_stats(game)

    for p in players:
        try:
            # General info
            playerInfo = []
            playerInfo.extend([p.player.player_id, p.player.name, p.team, p.player.position])

            # Player Weekly Info
            playerWeekInfo = []
            playerWeekInfo.extend([week, p.home])

            # Passing info
            playerPassing = []
            playerPassing.extend([p.passing_att, p.passing_cmp, p.passing_yds, p.passing_int, p.passing_tds,
                                  p.twopta, p.twoptm])

            # Receiving info
            playerReceiving = []
            playerReceiving.extend([p.receiving_tar, p.receiving_rec, p.receiving_yds, p.receiving_yac_yds,
                                    p.receiving_tds, p.twoptm])

            # Rushing info
            playerRushing = []
            playerRushing.extend([p.rushing_att, p.rushing_yds, p.rushing_rac_yds, p.rushing_tds, p.twoptm])

            # Misc. info
            playerMisc = []
            playerMisc.extend([p.fumbles_tot, p.fumbles_lost])

            playerStatLine = [playerInfo, playerWeekInfo, playerPassing, playerReceiving, playerRushing, playerMisc]
            yearStatLine.append(playerStatLine)

        except AttributeError:
            print str("Could not find info for ") + p.name
            pass

yearStatLine.sort()
for index in yearStatLine:
    print index

player = ET.Element("Player")
id = ET.SubElement(player, "ID")


# print yearStatLine

# nflgame.combine(nflgame.games(2016)).csv('season2010.csv')

# sys.stdout.write(str(p.player.player_id) + ',' + str(p.player.name) + ',' + str(p.team) + ',' + str(week) + ','
    # + str(p.home) + ',' + str(p.player.position) + '*')
# statLine = (str(p.player.player_id) + ',' + str(p.player.name) + ',' + str(p.team) + ',' + str(week) + ','
    # + str(p.home) + ',' + str(p.player.position) + '*')

# sys.stdout.write(str(p.passing_att) + ',' + str(p.passing_cmp) + ',' + str(p.passing_yds) + ',' + str(p.passing_int)
    # + ',' + str(p.passing_tds) + ',' + str(p.twopta) + ',' + str(p.twoptm) + ',')
# statLine += (str(p.passing_att) + ',' + str(p.passing_cmp) + ',' + str(p.passing_yds) + ',' + str(p.passing_int)
    # + ',' + str(p.passing_tds) + ',' + str(p.twopta) + ',' + str(p.twoptm) + ',')

# sys.stdout.write(str(p.receiving_tar) + ',' + str(p.receiving_rec) + ',' + str(p.receiving_yds) + ','
    # + str(p.receiving_yac_yds) + ',' + str(p.receiving_tds) + ',' + str(p.twoptm) + ',')
# statLine += (str(p.receiving_tar) + ',' + str(p.receiving_rec) + ',' + str(p.receiving_yds) + ','
    # + str(p.receiving_yac_yds) + ',' + str(p.receiving_tds) + ',' + str(p.twoptm) + ',')

# sys.stdout.write(str(p.rushing_att) + ',' + str(p.rushing_yds) + ',' + str(p.rushing_rac_yds) + ','
    # + str(p.rushing_tds) + ',' + str(p.twoptm) + ',')
# statLine += (str(p.rushing_att) + ',' + str(p.rushing_yds) + ',' + str(p.rushing_rac_yds) + ','
    # + str(p.rushing_tds) + ',' + str(p.twoptm) + ',')

# print(str(p.fumbles_tot) + ',' + str(p.fumbles_lost))
# statLine += (str(p.fumbles_tot) + ',' + str(p.fumbles_lost))