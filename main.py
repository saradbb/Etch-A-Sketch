from turtle import Turtle,Screen
#Simple Etch-A_Sketch Using Turtle
# KEYS AND WHAT THEY DO:
# W Move forward
# S Move Backward
# A counter-clockwise turn
# D clockwise turn
# C clear

sketch_turtle =Turtle()
def initialize_position():
    sketch_turtle.setheading(0)
    sketch_turtle.penup()
    sketch_turtle.goto(START_X_POS, START_Y_POS)
    sketch_turtle.pendown()


sketch_turtle.shape('turtle')
screen = Screen()
DISTANCE = 10  #The distance turtle draws in one key-press
ANGLE = 10 #The angle turtle turns when keys pressed
FORWARD_KEY = 'w'
BACKWARD_KEY = 's'
CLOCKWISE_KEY = 'd'
COUNTERCLOCK_KEY = 'a'
START_X_POS = 25
START_Y_POS = 25
CLEAR_KEY = 'c'
initialize_position()

def forward():
    sketch_turtle.forward(DISTANCE)
def backward():
    sketch_turtle.forward(-DISTANCE)
def clockwise():
    sketch_turtle.right(ANGLE)
def counterclockwise():
    sketch_turtle.left(ANGLE)
def clear():
    sketch_turtle.clear()
    initialize_position()


screen.listen()
screen.onkey(key = FORWARD_KEY,fun = forward)
screen.onkey(key = BACKWARD_KEY,fun = backward)
screen.onkey(key = CLOCKWISE_KEY, fun = clockwise )
screen.onkey(key = COUNTERCLOCK_KEY, fun = counterclockwise)
screen.onkey(key = CLEAR_KEY, fun = clear)



screen.exitonclick()