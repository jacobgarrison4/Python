"""
Earhquake Analysis
CIS 210 F17 project 8

Author: Jacob Garrison

Credits: Python PProgramming in Context

Uses Turtle Graphics to show earthquake data.
"""

from math import *
import turtle
import random

def main():
    """
    Sets values for k, r, and a file name.
    then calls visualizeQuakes with the set
    parameters.
    """
    k = 6
    r = 7
    f = 'earthquakes.txt'
    visualizeQuakes(k, r, f)
    
def readfile(file):
    """(file) -> dict

    Reads a file line by line and pulls out the
    longitude and latitude and stores it in a
    dictionary.

    >>> readfile(short_earthquakes.txt)
    {1: [129.2695, 36.0645], 2: [-174.6136, -17.4576],
    3: [-17.1484, -59.0385], 4: [154.4975, -6.1003]}
    """
    with open(file, 'r') as myf:
        myf.readline()
        datadict = {}
        key = 0
        for line in myf:
            values = line.split(',')
            key += 1
            lat = float(values[1])
            lon = float(values[2])
            datadict[key] = [lon, lat]

    return datadict

def euclidD(point1, point2):
    """(str) -> number

    euclidD returns the distance between
    two given points in any dimension.

    >>> euclidD('0','0')
    0.0
    >>> euclidD('2','5')
    3.0
    >>>euclidD('9','3')
    6.0
    """
    total = 0
    for index in range(len(point1)):
        diff = (point1[index] - point2[index]) ** 2
        total += diff

    euclidDistance = sqrt(total)

    return euclidDistance
    
def createCentroids(k, datadict):
    """(int, dict) -> list

    creates a list of unique integers
    which are random centroids for clusters.

    >>> createCentroids(3, {1:1,2 2:3,4 3:5,6 4:7,8 5:9,10}
    [4, 2, 3]
    """
    centroids = []
    count = 0
    centroid_keys = []

    while count < k:
        rkey = random.randint(1, len(datadict))
        if rkey not in centroid_keys:
            centroids.append(datadict[rkey])
            centroid_keys.append(rkey)
            count += 1

    return centroids

def createClusters(k, centroids, datadict, iterations):
    """(int, list, dict, int) -> list

    takes the number of clusters, the centroids list,
    the data dictionary, and the number of iterations
    and returns a list of the clusters.
    
    with centroids and datadict as above...
    >>> creatClusters(3, centroids, datadict, 2)
    [[2], [1, 4], [3]]
    """
    for iteration in range(iterations):
       #print("****Iteration", iteration, "****")
        clusters = []
        for i in range(k):
            clusters.append([])

        for key in datadict:
            distances = []
            for cl_index in range(k):
                dist = euclidD(datadict[key], centroids[cl_index])
                distances.append(dist)
            min_dist = min(distances)
            index = distances.index(min_dist)
            clusters[index].append(key)

        dimensions = len(datadict[1])
        for cl_index in range(k):
            sums = [0]*dimensions
            for key in clusters[cl_index]:
                data_points = datadict[key]
                for ind in range(2):
                    sums[ind] = sums[ind] + data_points[ind]
            for ind in range(len(sums)):
                cl_len = len(clusters[cl_index])
                if cl_len != 0:
                    sums[ind] /= cl_len
            centroids[cl_index] = sums

        """for c in clusters:
            print("CLUSTER")
            for key in c:
                print(datadict[key], end=" ")
            print()"""

    return clusters
    

def visualizeQuakes(k, r, dataFile):
    """(int, int, file) -> None

    visualizeQuakes takes a number of centroids,
    a number of iterations, and a file, and calls
    other auxillary functions for data analysis.
    Then calls eqDraw to draw everything.
    """
    datadict = readfile(dataFile)
    quakeCentroids = createCentroids(k, datadict)
    clusters = createClusters(k, quakeCentroids, datadict, r)
    eqDraw(k, datadict, clusters)
    return None
    
def eqDraw(k, eqDict, eqClusters):
    """(int, dict, list) -> Turtle graphics

    eqDraw opens the turtle module and draws the
    color coordinated clusters on a map of the
    world.
    """
    quakeT = turtle.Turtle()
    quakeWin = turtle.Screen()
    quakeWin.bgpic("worldmap.gif")
    quakeWin.screensize(1800, 900)

    wFactor = (quakeWin.screensize()[0]/2)/180
    hFactor = (quakeWin.screensize()[1]/2)/90

    quakeT.hideturtle()
    quakeT.up()
    quakeT.speed('fastest')

    colorlist = ['red', 'green', 'blue', 'orange', 'cyan', 'yellow']

    for clusterIndex in range(k):
        quakeT.color(colorlist[clusterIndex])
        for key in eqClusters[clusterIndex]:
            lon = eqDict[key][0]
            lat = eqDict[key][1]
            quakeT.goto(lon * wFactor, lat * hFactor)
            quakeT.dot()
    quakeWin.exitonclick()


main()
