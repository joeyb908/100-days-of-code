from turtle import Turtle
ALIGNMENT = "center"
MOVEMENT = False
FONT = ("bodoni mt", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ai_score = 0
        self.player_score = 0
        self.color("white")
        self.goto(0, -400)
        self.goto(0, 275)
        self.hideturtle()

    def display_score(self):
        self.write(f"Player: {self.player_score}    AI: {self.ai_score}", MOVEMENT, ALIGNMENT, FONT)

    def increase_ai_score(self):
        self.ai_score += 1
        self.clear()
        self.write(f"Player: {self.player_score}    AI: {self.ai_score}", MOVEMENT, ALIGNMENT, FONT)

    def increase_player_score(self):
        self.player_score += 1
        self.clear()
        self.write(f"Player: {self.player_score}    AI: {self.ai_score}", MOVEMENT, ALIGNMENT, FONT)