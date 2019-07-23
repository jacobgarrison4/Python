from math import *
def euclidD(point1, point2):
    total = 0
    for index in range(len(point1)):
        diff = (int(point1[index]) - int(point2[index])) ** 2
        total += diff

    euclidDistance = sqrt(total)
    print(euclidDistance)
    return euclidDistance
euclidD('0','0')
euclidD('2','5')
euclidD('9','3')
