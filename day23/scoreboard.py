from turtle import Turtle
import player
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-260, 250)
        self.level = 1
        self.write(f"Level: {self.level}", False, "left", FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.write(f"Score: {self.level}", False, "left", FONT)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game over. You got to level {self.level}", False, "center", FONT)
