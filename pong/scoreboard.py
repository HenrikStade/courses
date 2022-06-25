from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_l = 0
        self.score_r = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 200)
        self.write(arg=f"{self.score_l}", align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(arg=f"{self.score_r}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.clear()
    #     self.goto(0, 0)
    #     self.write(arg=f"Game over!", align=ALIGNMENT, font=FONT)

    def increase_score_l(self):
        self.score_l += 1
        self.clear()
        self.update_scoreboard()

    def increase_score_r(self):
        self.score_r += 1
        self.clear()
        self.update_scoreboard()
