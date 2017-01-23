import nflgame

weeks = [1, 2, 3]
yearStatLine = []

for week in weeks:
    game = nflgame.games(2016, week)
    players = nflgame.combine_play_stats(game)

    for p in players:
        try:
            # General info
            playerList = []
            playerList.append(p.player.player_id)
            playerList.append(p.player.name)
            playerList.append(p.team)
            playerList.append(week)
            playerList.append(p.home)
            playerList.append(p.player.position)

            # Passing info
            playerList.extend([p.passing_att, p.passing_cmp, p.passing_yds, p.passing_int, p.passing_tds, p.twopta, p.twoptm])

            # Receiving info
            playerList.extend([p.receiving_tar, p.receiving_rec, p.receiving_yds, p.receiving_yac_yds, p.receiving_tds, p.twoptm])

            # Rushing info
            playerList.extend([p.rushing_att, p.rushing_yds, p.rushing_rac_yds, p.rushing_tds, p.twoptm])

            # Misc. info
            playerList.extend([p.fumbles_tot, p.fumbles_lost])

            yearStatLine.append(playerList)

        except:
            # print p.name
            pass

yearStatLine.sort()
length = len(yearStatLine)

for index in length:
    if yearStatLine[index][0] == yearStatLine[index + 1][0]:
        catList = yearStatLine[index] + yearStatLine[index + 1]


print yearStatLine



# nflgame.combine(nflgame.games(2016)).csv('season2010.csv')

# sys.stdout.write(str(p.player.player_id) + ',' + str(p.player.name) + ',' + str(p.team) + ',' + str(week) + ',' + str(p.home) + ',' + str(p.player.position) + '*')
# statLine = (str(p.player.player_id) + ',' + str(p.player.name) + ',' + str(p.team) + ',' + str(week) + ',' + str(p.home) + ',' + str(p.player.position) + '*')

# sys.stdout.write(str(p.passing_att) + ',' + str(p.passing_cmp) + ',' + str(p.passing_yds) + ',' + str(p.passing_int) + ',' + str(p.passing_tds) + ',' + str(p.twopta) + ',' + str(p.twoptm) + ',')
# statLine += (str(p.passing_att) + ',' + str(p.passing_cmp) + ',' + str(p.passing_yds) + ',' + str(p.passing_int) + ',' + str(p.passing_tds) + ',' + str(p.twopta) + ',' + str(p.twoptm) + ',')

# sys.stdout.write(str(p.receiving_tar) + ',' + str(p.receiving_rec) + ',' + str(p.receiving_yds) + ',' + str(p.receiving_yac_yds) + ',' + str(p.receiving_tds) + ',' + str(p.twoptm) + ',')
# statLine += (str(p.receiving_tar) + ',' + str(p.receiving_rec) + ',' + str(p.receiving_yds) + ',' + str(p.receiving_yac_yds) + ',' + str(p.receiving_tds) + ',' + str(p.twoptm) + ',')

# sys.stdout.write(str(p.rushing_att) + ',' + str(p.rushing_yds) + ',' + str(p.rushing_rac_yds) + ',' + str(p.rushing_tds) + ',' + str(p.twoptm) + ',')
# statLine += (str(p.rushing_att) + ',' + str(p.rushing_yds) + ',' + str(p.rushing_rac_yds) + ',' + str(p.rushing_tds) + ',' + str(p.twoptm) + ',')

# print(str(p.fumbles_tot) + ',' + str(p.fumbles_lost))
# statLine += (str(p.fumbles_tot) + ',' + str(p.fumbles_lost))