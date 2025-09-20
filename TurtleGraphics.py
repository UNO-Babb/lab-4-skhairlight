#TurtleGraphics.py
#Name: Salsabiel Khair Allah
#Date: Sep.20
#Assignment: Lab 4

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(myTurtle, sides, size=100):
    #Draws a polygon with the given number of sides.
    angle = 360 / sides
    for _ in range(sides):
        myTurtle.forward(size)
        myTurtle.right(angle)

def fillCorner(myTurtle, corner, size=100):
    drawSquare(myTurtle, size)
    half = sixe / 2
    if corner == 1:
        myTurtle.penup()
        myTurtle.goto(-half, half)
    elif corner == 2:
        myTurtle.penup()
        myTurtle.goto(0, half)
    elif corner == 3:
        myTurtle.penup()
        myTurtle.goto(-half, 0)
    elif corner == 4:
        myTurtle.penup()
        myTurtle.goto(0,0)
    
    myTurtle.pendown()
    myTurtle.begin_fill()
    for _ in range(4):
        myTurtle.forward(half)
        myTurtle.right(90)
    myTurtle.end_fill()

def squaresInSquares(myTurtle, num, size=200):
    step = size / num
    for i in range(num):
        drawSquare(myTurtle, size - i * step)
        myTurtle.penup()
        myTurtle.forward(step / 2)
        myTurtle.right(90)
        myTurtle.forward(step / 2)
        myTurtle.left(90)
        myTurtle.pendown()


def main():
    myTurtle = turtle.Turtle()
    myTurtle.speed(3)
    turtle.done
    # drawPolygon(myTurtle, 5) #draws a pentagon
    # drawPolygon(myTurtle, 8) #draws an octogon

    # fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
