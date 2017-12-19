color1 = input("Enter color 1: ")
color2 = input("Enter color 2: ")

import turtle
start = "0, 0"
turtle.speed(0)

turtle.goto(0, 0)
def drawSquare(color):
    turtle.down()
    turtle.color(color)
    for i in range(4):
        turtle.forward(20)
        turtle.left(90)

def drawRow(color1, color2):
    turtle.setheading(0)
    for i in range(4):
        turtle.begin_fill()
        drawSquare(color=(color1))
        turtle.end_fill()
        turtle.up()
        turtle.forward(40)
    turtle.backward(180)
    for i in range(4):
        turtle.forward(40)
        turtle.begin_fill()
        drawSquare(color=(color2))
        turtle.end_fill()
        turtle.up()
    turtle.backward(140)
    turtle.setheading(90)
    turtle.forward(20)




def drawGrid():
    for i in range(4):
        drawRow(color1=color1, color2=color2)
        drawRow(color1=color2, color2=color1)

drawGrid()