from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()


