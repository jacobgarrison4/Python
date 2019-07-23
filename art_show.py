"""
Art Show
CIS 210 F17 Project 2
Author: Jacob Garrison
Credits: N/A
"""
from turtle import *

def square1(length):
    '''(int) -> None

    draws a square with each side equal to 'length'

    >>>square1(50)
    '''
    position()
    fd(length)
    lt(90)
    fd(length)
    lt(90)
    fd(length)
    lt(90)
    fd(length)
    return None

def square2(length,scolor):
    '''(int, color) -> None

    draws a square with each side equal to 'length' and is colored

    >>>square2(25, red)
    '''
    begin_fill()
    color(scolor)
    position()
    fd(length)
    lt(90)
    fd(length)
    lt(90)
    fd(length)
    lt(90)
    fd(length)
    end_fill()
    return None

def triangle(length,tcolor):
    '''(int, color) -> None

    draws a colored triangle with each side equal to 'length'

    >>>triangle(75,blue)
    '''
    begin_fill()
    color(tcolor)
    fd(length)
    lt(120)
    fd(length)
    lt(120)
    fd(length)
    end_fill()
    return None

def art_show():
    '''() -> None

    draws a house with a door and a roof

    >>>house()
    '''
    triangle(200, 'gray')
    lt(30)
    square1(200)
    lt(90)
    fd(200)
    lt(90)
    fd(60)
    square2(85, 'brown')
    return None
