import matplotlib
from matplotlib import pyplot
import numpy as np
import math
def scatterploat(filename):
    f=[i.strip("\n") for i in open(filename,"r").readlines()]
    #f.remove("")
    d=map(float,f)
    mean=sum(d)/len(d)

    print("mean of data:"+str(mean))

    d3=d[1:]
    d3+=[4]
    pyplot.scatter(d, d3)
    pyplot.title('Scatter plot ')
    pyplot.xlabel('x')
    pyplot.ylabel('y')
    pyplot.show()

def getInrange(arr,minn,maxx):
    k=0
    for i in arr:
        if(i>=minn and i<maxx ):
            k+=1
    return k

def drawBarChart(filename,intervals):
    f=[i.strip("\n") for i in open(filename,"r").readlines()]
    #f.remove("")
    d=map(float,f)
    minn=min(d)
    minnn=minn
    maxx=max(d)
    diff=(maxx-minn)/intervals
    data=[]
    while(minn<maxx):
        data.append((minn,minn+diff,getInrange(d,minn,minn+diff)))
        minn+=diff
    print(data)
    freq=[i[2] for i in data]
    print("frequency")
    print(freq)
    print("minn"+str(minnn))
    print("maxx"+str(maxx))
    print("diff"+str(diff))
    xp=np.arange(minnn,maxx,diff)
    print(xp)
    pyplot.bar(xp,freq,1)
    pyplot.show()
drawBarChart("requestdata.txt",260)
scatterploat("requestdata.txt")