from turtle import Turtle
ALIGNMENT = "center"
MOVEMENT = False
FONT = ("bodoni mt", 16, "normal")


# scoreboard with superclass of turtle since it's an object on screen
class Scoreboard(Turtle):

    def __init__(self, saved_high_score):
        super().__init__()
        self.score = 0
        self.high_score = saved_high_score
        self.goto(0, 270)
        self.hideturtle()
        self.color("white")
        self.display_score()

    def display_score(self):
        self.write(f"Score: {self.score} High Score: {self.high_score}", MOVEMENT, ALIGNMENT, FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.display_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game over", MOVEMENT, ALIGNMENT, FONT)
    #     self.clear()
    #

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.score = 0
            self.clear()
            self.display_score()
            with open("high_scores.txt", mode="w") as file:
                # can alternatively do the following:
                # file.write(f"{self.high_score}") to turn into a string
                file.write(str(self.high_score))

        else:
            self.score = 0
            self.clear()
            self.display_score()
