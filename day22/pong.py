from turtle import Turtle
CENTER = (0, 0)

class Pong(Turtle):
    def __init__(self):
        super().__init__()
        self.pong_ball = []
        self.add_ball()

    def add_ball(self):
        pong_ball = Turtle(shape="square")
        pong_ball.speed("fastest")
        pong_ball.penup()
        pong_ball.shapesize(stretch_len=.5, stretch_wid=.5)
        pong_ball.color("white")
        pong_ball.goto(CENTER)
        self.pong_ball.append(pong_ball)

    def move(self):
