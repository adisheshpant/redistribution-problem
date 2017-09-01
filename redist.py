import matplotlib.pyplot as plt
import matplotlib.animation as animation 
import numpy as np

LEN=100
UNIT=45
data = [UNIT]*LEN
x = range(len(data))

def buildPlot(fig, dim):
    ax = fig.add_subplot(dim)
    ax.fill()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    return ax

def animate(i):
    # process X records per frame
    for j in range(500): process()
    animatePlot2()
    animatePlot1()

def prepare(ax):
    ax.clear()
    ax.grid(True)
    ax.set_ylim([0,UNIT*3.5])

def animatePlot1():
    # sorted bar
    d = sorted(data)
    prepare(ax1)
    ax1.bar(x, d, color='#3F5D7D')

def animatePlot2():
    # line 
    prepare(ax2)
    ax2.plot(x, data, color='#3F5D7D')

def process():
    """
    Redistribute data. Pick a random receiver and
    a random sender who has funds > 0
    """ 
    receiver = np.random.randint(0, LEN-1)
    sender = receiver
    while sender == receiver or data[sender] <= 0:
        sender = np.random.randint(0, LEN-1)
    data[receiver] += 1
    data[sender] -= 1

fig = plt.figure()
ax1 = buildPlot(fig, 211)
ax2 = buildPlot(fig, 212)

ani = animation.FuncAnimation(fig, animate, interval=5)

plt.show()
