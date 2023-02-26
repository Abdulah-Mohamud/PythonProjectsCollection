from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game!!")
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-30, 0)]

segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.goto(position)
    segments.append(new_segment)

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)

    for seg in range(len(segments) - 1, 0, -1):
        new_x = segments[seg - 1].xcor()
        new_y = segments[seg - 1].ycor()
        segments[seg].goto(new_x, new_y)

    segments[0].forward(20)



    if new_segment.xcor() > 600 or new_segment.xcor() < -600 or new_segment.ycor() < -600 or new_segment.ycor() > 600:
        game_on = False
        print("Game Over")



screen.exitonclick()


