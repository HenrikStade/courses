from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
STARTING_POSITIONS = [(-350, 0), (350, 0)]

screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_r = Paddle(STARTING_POSITIONS[1])
paddle_l = Paddle(STARTING_POSITIONS[0])
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_r.up, "Up")
screen.onkey(paddle_r.down, "Down")
screen.onkey(paddle_l.up, "w")
screen.onkey(paddle_l.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision wit top / bottom:
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Detect collision with right paddle:
    if ball.distance(paddle_r) < 50 and ball.xcor() > 340:
        ball.bounce_x()

    # Detect collision with left paddle:
    if ball.distance(paddle_l) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    # Detect left player scores:
    if ball.xcor() > 380:
        scoreboard.increase_score_l()
        ball.reset_position()

    # Detect right player scores:
    if ball.xcor() < -380:
        scoreboard.increase_score_r()
        ball.reset_position()


screen.exitonclick()
