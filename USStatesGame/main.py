import turtle

import pandas as pd
from turtle import Turtle, Screen

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df = pd.read_csv("50_states.csv")

all_states = df["state"].tolist()

while len(all_states) > 0:
    user_guess = screen.textinput(title="", prompt="Name an American state:").title()
    if user_guess == "Exit":
        df = pd.DataFrame(all_states)
        df.to_csv("missing_states.csv")
        exit()
    if user_guess in all_states:
        state = df[df.state == user_guess]

        state_pos = (int(state.x), int(state.y))

        t = Turtle()
        t.penup()
        t.hideturtle()
        t.goto(state_pos)
        t.write(state.state.item())  # user_guess)#str(state.iloc[0]["state"]))

        all_states.remove(user_guess)
    # else:
    #     user_guess = screen.textinput(title="", prompt="Name an American state:").capitalize()

screen.exitonclick()
