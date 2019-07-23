from turtle import *
import random
'''
def circle_draw(x):
    reset()
    begin_fill()
    color('green', 'gold')
    circle(x)
    end_fill()
    return #None

circle_draw(20)
'''
def move():
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    setposition(x,y)
    stamp()
    return #None

reset()
shape('square')
bgcolor('black')
color('blue','yellow')
move()
move()
move()
move()
move()
