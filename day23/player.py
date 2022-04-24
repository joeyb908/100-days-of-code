from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_VECTOR = [0, 20]
MOVE_VECTOR_X = MOVE_VECTOR[0]
MOVE_VECTOR_Y = MOVE_VECTOR[1]
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def player_rules(self):
        self.reset()

    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_VECTOR_Y)

    def reset(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.goto(STARTING_POSITION)

