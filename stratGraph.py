"""
Strategy Graph and plotting class
"""
import matplotlib.pyplot as plt

#plot the strategies on a graph
def plotStrategies(strats):

    plt.figure(figsize = (10,6))

    for s in strats:

        label = f"{s['strategy']}"

        plt.plot(res["lapTimes"], label = label)

    plt.xlabel("Lap")
    plt.ylabel("Lap Time (secs)")
    plt.title("Race Strategy Simulation")
    plt.legend()
    plt.show()
