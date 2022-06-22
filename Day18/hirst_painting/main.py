import colorgram
import turtle as tm
from math import floor
import random

colors = colorgram.extract('image.jpg', 30)

rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    if not all([floor(r / 230), floor(g / 230), floor(b / 230)]):
        rgb_colors.append(new_color)

color_list = rgb_colors

timmy = tm.Turtle()
timmy.shape("turtle")
timmy.hideturtle()
timmy.penup()
timmy.speed("fastest")
tm.colormode(255)

timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
no_of_dots = 100

for dot in range (1,no_of_dots + 1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)

    if dot % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen = tm.Screen()
screen.exitonclick()

