from turtle import Turtle
import random as r


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color('yellow')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        self.goto(r.randint(-280, 280), r.randint(-280, 280))
