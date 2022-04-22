from turtle import Turtle
ALIGNMENT = "center"
MOVEMENT = False
FONT = ("bodoni mt", 16, "normal")


# scoreboard with superclass of turtle since it's an object on screen
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 270)
        self.hideturtle()
        self.color("white")
        self.display_score()

    def display_score(self):
        self.write(f"Score: {self.score}", MOVEMENT, ALIGNMENT, FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", MOVEMENT, ALIGNMENT, FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over", MOVEMENT, ALIGNMENT, FONT)
