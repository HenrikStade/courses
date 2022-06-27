import pandas as pd
from turtle import Turtle, Screen

screen = Screen()
screen.bgpic("blank_states_img.gif")

df = pd.read_csv("50_states.csv")

user_guess = screen.textinput(title="", prompt="Name an American state:").lower()
print(user_guess)

state = df[df["state"]. == "alabama"]
print(state)
state_pos = (int(state.x), int(state.y))

timmy = Turtle()
timmy.penup()
timmy.write(str(state.iloc[0]["state"]))
timmy.hideturtle()
timmy.goto(state_pos)



screen.exitonclick()
