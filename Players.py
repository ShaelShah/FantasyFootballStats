

class Player:

    id = 0
    name = ""
    weeklyStats = []

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def addweeklystatline(self, statline):
        self.weeklyStats.append(statline)

    def printstats(self):
        print self.id
        print self.name

        for week in self.weeklyStats:
            for statline in week:
                print statline.printstatline()


class Stats:

    def __init__(self):
        print "Parent"

    def printstatline(self):
        print "I printed stats"


class WeekInfo(Stats):

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

    def printstatline(self):
        print "week info printstatline"


class PassingStats(Stats):

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
        self.passingTwoPts = passingtwopts
        self.passingTwoPtAtts = passingtwoptatts

    def printstatline(self):
        print "passing stats printstatline"


class ReceivingStats(Stats):

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

    def printstatline(self):
        print "receiving stats printstatline"


class RushingStats(Stats):

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

    def printstatline(self):
        print "rushing stats printstatline"


class MiscStats(Stats):

    fumbles = 0
    fumblesLost = 0

    def __init__(self, fumbles, fumbleslost):
        self.fumbles = fumbles
        self.fumblesLost = fumbleslost

    def printstatline(self):
        print "misc stats printstatline"

