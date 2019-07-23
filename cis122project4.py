from turtle import *
import random

#Problem 0
def sun_and_earth():
    '''() -> None
draws the sun and the earth with relative sizes

>>>sun_and_earth()
'''
    begin_fill()
    color('yellow')
    circle(109)
    end_fill()
    penup()
    setpos(200,0)
    begin_fill()
    color('blue')
    circle(1)
    end_fill()
    penup()
    setpos(100,-100)
    return #None

#Problem 1a
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
    return #None

#Problem 1b
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
    return #None

#Problem 1c
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
    return #None

#Problem 1d
def house():
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
    return #None

#Problem 2a
def mars_explore_main():
    '''() -> None

    main function for mars_explore:
        set up print and graphical output
        then call mars_explore repeatedly

    data is printed; None value is returned

    >>> mars_explore_main()
    '''
    # label for print output   
    print("xpos", "\t",
          "ypos", "\t",
          "water", "\t",
          "temp")           

    # set up graphical output
    reset()
    title("Mars Rover")
    display_color = "blue"
    color(display_color)
    shape('square')
    stamp()   # draw the rover

    # explore five places on Mars
    
    mars_explore()
    mars_explore()
    mars_explore()
    mars_explore()
    mars_explore()
    
def rover_loc():
    '''() -> int
return random number for rover location

>>>rover_loc()
120
'''
    return random.randint(-275,275)

def water_content():
    '''() -> int
return random number for water content in ppm

>>>water_content()
56
'''
    return random.randint(1,290)

def temperature():
    '''() -> int
return random number for temperature in fahrenheit

>>>temp()
-107
'''
    return random.randint(-178,1)

def mars_explore():
    '''() -> (int, int, int, int)
return random numbers for location, water content and temperature

>>>mars_explore
7 -54 128 -120
'''
    x = rover_loc()
    y = rover_loc()
    xpos = x
    ypos = y
    water = water_content()
    temp = temperature()
    setposition(x,y)
    stamp()
    print(xpos, '\t', ypos, '\t', water, '\t', temp)
    return #None
