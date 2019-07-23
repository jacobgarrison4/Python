import turtle

def drawSquare(numSquares, sideLength):
    for i in range(4):
        turtle.forward(sideLength)
        turtle.right(90)

def drawflower(numSquares, sideLength):
    turtle.speed(0)
    for i in range(numSquares):
        drawSquare(numSquares, sideLength)
        turtle.right(360/numSquares)
    
