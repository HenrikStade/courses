from turtle import Turtle, Screen
import random

is_race_on = False
# Set up the screen
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
user_bet = screen.textinput(title="Make your bet:", prompt=f"Which turtle will win the race? "
                                                           f"Enter a color:\n{colors} ").lower()
if user_bet not in colors:
    user_bet = screen.textinput(title="Color not is list, try again.",
                                prompt=f"Which turtle will win the race? Enter a color:\n{colors} ").lower()
if user_bet:
    is_race_on = True

turtles = []
for turtle_index in range(0, len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    pos_x = (-screen.window_width() / 2) * 0.9
    y_lower = (-screen.window_height() / 2) * 0.8
    y_upper = (screen.window_height() / 2) * 0.8
    pos_y = ((-screen.window_height() / 2) * 0.8) + ((y_upper - y_lower) / (len(colors)-1)) * turtle_index
    new_turtle.goto(pos_x, pos_y)
    turtles.append(new_turtle)

while is_race_on:
    for turtle in turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

        if turtle.xcor() >= (screen.window_width() / 2) - 20:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You have won! The {winner} turtle is the winner!")
            else:
                print(f"You have lost! The {winner} turtle is the winner!")

screen.exitonclick()
