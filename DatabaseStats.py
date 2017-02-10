import GetStats

# playerList = GetStats.updatestats(False, False, False)
playerListData = GetStats.getpickledata()

# print len(playerList)
print len(playerListData)

# print playerList[0].gettotalweeks()
print playerListData[0].getinfo()
print playerListData[0].gettotalweeks()
# for player in playerList:
#     print player.getinfo() + str(" - ") + str(player.gettotalweeks())


