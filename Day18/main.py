import turtle
from turtle import Turtle, Screen
import random


def change_color(turtle):
    r = random.random()
    b = random.random()
    g = random.random()
    turtle.color(r, g, b)


def new_color(turtle):
    if random.randint(0, 101) > 40:
        change_color(turtle)


timmy = Turtle()
timmy.shape("turtle")
# timmy.color("chartreuse3")

# for i in range(1, 5):
#     timmy.forward(100)
#     timmy.right(90)

# Draw a dashed line
# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()
#
# # Draw shapes in one
# change_color(timmy)
# for angle in range(3, 9):
#     for _ in range(angle):
#         timmy.forward(150)
#         timmy.right(360/angle)
#     change_color(timmy)

# Random Walk
# timmy.pensize(20)
# change_color(timmy)
# for _ in range(100):
#     timmy.forward(30)
#     timmy.right(90 * random.randint(-1, 1))
#     new_color(timmy)

# Spirograph


def draw_spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        new_color(timmy)
        timmy.circle(100)
        timmy.setheading(timmy.heading() + gap_size)


timmy.speed("fastest")
draw_spirograph(5)


















screen = Screen()
screen.exitonclick()
