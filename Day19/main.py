from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
timmy.shape("arrow")


def move_forwards():
    timmy.forward(10)


def move_backwards():
    timmy.backward(10)


def turn_counterclockwise():
    timmy.setheading(timmy.heading() + 15)


def turn_clockwise():
    timmy.setheading(timmy.heading() - 15)


def clear_screen():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_counterclockwise)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()