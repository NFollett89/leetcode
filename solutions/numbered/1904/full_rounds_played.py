# https://leetcode.com/problems/the-number-of-full-rounds-you-have-played/

class Solution:
    def __init__(self, incrementMinutes=15):
        self.incrementMinutes = incrementMinutes

    def getTotalMinutes(self, time: str) -> int:
        parts = time.split(":")
        hours = int(parts[0])
        minutes = int(parts[1])
        return hours * 60 + minutes

    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        loginMinutes = self.getTotalMinutes(loginTime)
        if loginMinutes % self.incrementMinutes == 0:
            firstRound = loginMinutes
        else:
            firstRound = loginMinutes + (self.incrementMinutes - loginMinutes % self.incrementMinutes)
        logoutMinutes = self.getTotalMinutes(logoutTime)
        if logoutTime < loginTime:
            timePlayed = (24 * 60) - firstRound + logoutMinutes
        else:
            timePlayed = logoutMinutes - firstRound
        totalRounds = max(timePlayed // self.incrementMinutes, 0)
        return totalRounds
