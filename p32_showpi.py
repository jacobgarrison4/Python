"""
Show Monte Pi
CIS 210 F17 Project 3

Authors: Jacob Garrison

Credits: Python Programming in Context

Shows a vizualization of the monte pi algorithm
and returns a report of our approximation
along with a percentage error with the math lib
sqrt value.
"""

from p3_approxpi import *
from turtle import *
from random import *
import math

def showMontePi(numDarts):
    """(int) -> float

    Returns an approximation for pi and uses
    Turtle graphics to display a visual
    representation. Also prints a report with
    a percentage error.

    >>> showMontePi(1000)
    With 50  iterations: 
    my approximate value for pi is:  3.28 
    math lib pi value is:  3.141592653589793 
    This is a  4.41 percent error.
    """
    wn = Screen()
    drawingT = Turtle()

    wn.setworldcoordinates(-2,-2,2,2)

    drawingT.up()
    drawingT.goto(-1,0)
    drawingT.down()
    drawingT.goto(1,0)

    drawingT.up()
    drawingT.goto(0,1)
    drawingT.down()
    drawingT.goto(0,-1)

    count = 0

    drawingT.up()

    for i in range(numDarts):
        x = random()
        y = random()
        r = 1
        drawingT.goto(x,y)

        if isinCircle(x,y,r):
            count += 1
            drawingT.color("blue")
        else:
            drawingT.color("red")

        drawingT.dot()

    pi = ( count / numDarts ) * 4

    pe = round( ( abs( pi - math.pi ) / math.pi ) * 100, 2 )

    print("With", numDarts, " iterations: \nmy approximate value for pi is: ",
          pi, "\nmath lib pi value is: ", math.pi, "\nThis is a ", pe, "percent error.")

    wn.exitonclick()

    return pi
