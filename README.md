# Redistribution problem


I found this interesting [experiment](http://www.decisionsciencenews.com/2017/06/19/counterintuitive-problem-everyone-room-keeps-giving-dollars-random-others-youll-never-guess-happens-next/) where random redistrubtion of data in a closed system leads to very unique patterns. I've attempted to recreate this with python in matplotlib.

In every iteration each node sends an unit of value to another randomly chosen node. As this process continues the wealth distribution takes on a very interesting shape. Instead of the wealth being randomly distributed, only a few nodes end up being the most wealthy, and the accumulation of wealth tapers off logarithmically. Note that the 'wealthiest' nodes keep rotating. Eventually over time all nodes will at some point be the wealthiest nodes, but the distribution pattern remains constant.

![Alt text](/ani.gif?raw=true)
