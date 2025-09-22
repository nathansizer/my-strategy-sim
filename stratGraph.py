"""
Strategy Graph and plotting class
"""
import matplotlib.pyplot as plt
import numpy as np

#plot the strategies on a graph
def plotStrategies(strats):

    plt.figure(figsize = (10,6))

    totalTimes = [np.cumsum(s["lapTimes"]) for s in strats]

    baseline = np.min(np.vstack(totalTimes), axis = 0)

    for i, s in enumerate(strats):

        gap = totalTimes[i] - baseline
        plt.plot(range(1, len(gap) + 1), gap, label = f"{s['strategy']}")

        for p in s["strategy"].pitLaps:
            plt.scatter(p, gap[p-1], color = plt.gca().lines[-1].get_color(), marker = "x", s = 60, zorder = 3, label = None)

    plt.xlabel("Lap")
    plt.ylabel("Gap to fastest strategy (secs)")
    plt.title("Race Strategy Simulation")
    plt.legend()
    plt.show()
