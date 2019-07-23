"""
Monte Pi
CIS 210 F17 Project 3

Authors: Jacob Garrison

Credits: Python Programming in Context

Computes an approximation of pi using the
Monte Carlo algorithm.
"""

from math import *
from random import *

def isinCircle(x,y,r):
    """(int,int,int) -> bool

    Returns True if the input point is
    inside the circle centered at (0,0)
    with radius r, and False otherwise.

    >>> isincircle(0,0,1)
    True
    >>> isinCircle(.5,.5,1)
    True
    >>> isinCircle(1,2,1)
    False
    """

    distance = sqrt( x ** 2 + y ** 2 )
    if r >= distance:
        return True
    else:
        return False

def montePi(numDarts):
    """(int) -> float

    Returns the approximate value for pi.

    >>> montePi(100)
    3.08
    >>> montePi(100000)
    3.143072
    >>> montePi(10000000)
    3.1418752
    """

    count = 0
    
    for i in range(numDarts):
        x = random()
        y = random()
        r = 1

        if isinCircle(x,y,r):
            count += 1

    pi = ( count / numDarts ) * 4

    return pi


print(montePi(100))
print(montePi(100000))
print(montePi(10000000))
