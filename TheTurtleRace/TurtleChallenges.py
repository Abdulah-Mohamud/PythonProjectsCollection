from turtle import *
import random

# movement_done = True
screen = Screen()
my_turtle = Turtle(shape="turtle")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]


# creating a square
def shape(sides, length):
    for item in range(sides):
        angle = 360 / sides
        my_turtle.forward(length)
        my_turtle.right(angle)


def multi_shape(total_sides):
    sides = 3
    length = 100
    while total_sides != sides:
        color()
        shape(sides, length)
        sides += 1

def color():
    my_turtle.color(random.choice(colours))

my_turtle.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)



#s = 10
#multi_shape(s)

# steps = int(input("How big will you square be? "))
# square(steps)
screen.exitonclick()
