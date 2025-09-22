"""
The main file of the project.

Everything is run from here, simulations are compared and the best is printed.
"""

from race import Race
from strategy import Strategy
from stratGraph import plotStrategies


#define a race, here using the same parameters set out in the readme file
race = Race(52, 92.0, 25.0)

#define some strategies
strategies = [

    Strategy([25], ["medium", "hard"]),
    Strategy([15, 30], ["soft", "soft", "hard"]),
    Strategy([18, 34], ["soft", "medium", "medium"]),
    Strategy([13, 26, 39], ["soft", "soft", "soft", "soft"])

]

#work out race time results
results = []

for s in strategies:
        
    time, laps = race.simStrategy(s)
    results.append({"strategy": s, "time": time, "lapTimes": laps})

bestStrategy = min(results, key = lambda x: x["time"])

print("Fastest Strategy: ", bestStrategy["strategy"])
print("Total Race Time: ", round(bestStrategy["time"], 2), " seconds")

plotStrategies(results)
