"""
My Race class.
"""

from tyre import tyreSets
from strategy import Strategy

class Race:

    #initialiser
    def __init__(self, laps, baseLapTime, pitlaneLoss):

        self.laps = laps
        self.baseLapTime = baseLapTime
        self.pitlaneLoss = pitlaneLoss

    #sim a single lap given the tyre and it's age
    def simLap(self, tyre, age):

        return self.baseLapTime + tyre.degModifier(age)

    #sim a whole stint on a set of tyres
    def simStint(self, start, end, tyre):

        stintTime = 0
        laps = []

        for lap in range(start, (end + 1)):

            age = lap - start
            lapTime = self.simLap(tyre, age)
            stintTime += lapTime
            laps.append(lapTime)

        return stintTime, laps

    #sim a whole race strategy
    def simStrategy(self, strategy: Strategy):

        totalTime = 0
        everyLap = []
        currentLap = 1

        for i in range(len(strategy.pitLaps) + 1):

            if i < len(strategy.pitLaps):
                endStint = strategy.pitLaps[i]
            else:
                endStint = self.laps

            stintTime, stintLaps = self.simStint(currentLap, endStint, strategy.tyreOrder[i])
            totalTime += stintTime
            everyLap.extend(stintLaps)

            if i < len(strategy.pitLaps):
                everyLap[-1] += self.pitlaneLoss
                totalTime += self.pitlaneLoss

            currentLap = endStint + 1

        return totalTime, everyLap
        
