"""
Strategy Graph and plotting class
"""
import matplotlib.pyplot as plt
import numpy as np

#plot the strategies on a graph
def plotStrategies(strats):

    plt.figure(figsize = (10,6))

    for s in strats:

        label = f"{s['strategy']}"

        totalTime = np.cumsum(s["lapTimes"])
        plt.plot(range(1, len(totalTime) + 1), totalTime, label = label)

    plt.xlabel("Lap")
    plt.ylabel("Lap Time (secs)")
    plt.title("Race Strategy Simulation")
    plt.legend()
    plt.show()
