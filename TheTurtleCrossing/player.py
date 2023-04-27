from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280



bob = Turtle
bob.color("white")

class Player(Turtle):
    def __init__(self):
        super().__init__()
