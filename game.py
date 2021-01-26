from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Game(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.start_on = False

    def start_game(self):
        self.start_on = True

    def home_start(self):
        self.goto(0, -150)
        self.write('Press "space" to start', align=ALIGNMENT, font=FONT)
