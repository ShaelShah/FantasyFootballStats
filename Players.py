

class Player:

    id = 0
    name = ""
    weeklyStats = []

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def addweeklystatline(self, statline):
        self.weeklyStats.append(statline)

    def getinfo(self):
        return self.id + str(": ") + self.name

    def getweeklystats(self):
        return self.weeklyStats

    # def getstats(self):
    #     for week in self.weeklyStats:
    #         print len(week)
    #         for statline in week:
    #             return statline.getstatline()

    def gettotalweeks(self):
        return len(self.weeklyStats)

    def printcsv(self):
        return str(self.id) + "," + self.name


class WeekInfo:

    team = ""
    position = ""
    year = 0
    week = 0
    home = False

    def __init__(self, team, position, year, week, home):
        self.team = team
        self.position = position
        self.year = year
        self.week = week
        self.home = home

    def getstatline(self):
        return [self.team, self.position, self.year, self.week, self.home]

    def printcsv(self):
        return self.team + "," + self.position + "," + str(self.year) + "," + str(self.week) + "," + str(self.home)


class PassingStats:

    passingAttemps = 0
    passingCompletions = 0
    passingYards = 0
    passingInts = 0
    passingTDs = 0
    passingTwoPts = 0
    passingTwoPtAtts = 0

    def __init__(self, passingattempts, passingcompletions, passingyards, passingints, passingtds,
                 passingtwopts, passingtwoptatts):
        self.passingAttemps = passingattempts
        self.passingCompletions = passingcompletions
        self.passingYards = passingyards
        self.passingInts = passingints
        self.passingTDs = passingtds
        self.passingTwoPtAtts = passingtwoptatts
        self.passingTwoPts = passingtwopts

    def getstatline(self):
        return [self.passingAttemps, self.passingCompletions, self.passingYards, self.passingInts, self.passingTDs, self.passingTwoPtAtts, self.passingTwoPts]

    def printcsv(self):
        return str(self.passingAttemps) + "," + str(self.passingCompletions) + "," + str(self.passingYards) + "," + str(self.passingInts) + "," + str(self.passingTDs) + "," + str(self.passingTwoPtAtts) + "," + str(self.passingTwoPts)


class ReceivingStats:

    receivingTargets = 0
    receivingReceptions = 0
    receivingYards = 0
    receivingYardsAfterCatch = 0
    receivingTDs = 0
    receivingTwoPts = 0

    def __init__(self, receivingtargets, receivingreceptions, receivingyards, receivingyardsaftercatch,
                 receivingtds, receivingtwopts):
        self.receivingTargets = receivingtargets
        self.receivingReceptions = receivingreceptions
        self.receivingYards = receivingyards
        self.receivingYardsAfterCatch = receivingyardsaftercatch
        self.receivingTDs = receivingtds
        self.receivingTwoPts = receivingtwopts

    def getstatline(self):
        return [self.receivingTargets, self.receivingReceptions, self.receivingYards, self.receivingYardsAfterCatch, self.receivingTDs, self.receivingTwoPts]

    def printcsv(self):
        return str(self.receivingTargets) + "," + str(self.receivingReceptions) + "," + str(self.receivingYards) + "," + str(self.receivingYardsAfterCatch) + "," + str(self.receivingTDs) + "," + str(self.receivingTwoPts)


class RushingStats:

    rushingAttempts = 0
    rushingYards = 0
    rushingYardsAfterContact = 0
    rushingTDs = 0
    rushingTwoPts = 0

    def __init__(self, rushingattempts, rushingyards, rushingyardsaftercontact, rushingtds, rushingtwopts):
        self.rushingAttempts = rushingattempts
        self.rushingYards = rushingyards
        self.rushingYardsAfterContact = rushingyardsaftercontact
        self.rushingTDs = rushingtds
        self.rushingTwoPts = rushingtwopts

    def getstatline(self):
        return [self.rushingAttempts, self.rushingYards, self.rushingYardsAfterContact, self.rushingTDs, self.rushingTwoPts]

    def printcsv(self):
        return str(self.rushingAttempts) + "," + str(self.rushingYards) + "," + str(self.rushingYardsAfterContact) + "," + str(self.rushingTDs) + "," + str(self.rushingTwoPts)


class MiscStats:

    fumbles = 0
    fumblesLost = 0

    def __init__(self, fumbles, fumbleslost):
        self.fumbles = fumbles
        self.fumblesLost = fumbleslost

    def getstatline(self):
        return [self.fumbles, self.fumblesLost]

    def printcsv(self):
        return str(self.fumbles) + "," + str(self.fumblesLost)


