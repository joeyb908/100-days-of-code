from turtle import Turtle
PLAYER_STARTING_POSITION = (-370, 0)
AI_STARTING_POSITION = (370, 0)
DEFAULT_STARTING_POSITIONS = [(-370, 0), (370, 0)]
UP = 90
DOWN = -90
MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self, type):
        super().__init__()
        self.paddle_list = []
        self.type = type
        self.create_paddle(type)


    def add_paddle(self, position):
        new_paddle = Turtle(shape="square")
        new_paddle.speed("fastest")
        new_paddle.penup()
        new_paddle.shapesize(stretch_len=.5, stretch_wid=2)
        new_paddle.color("white")
        new_paddle.goto(position)
        self.paddle_list.append(new_paddle)

    def create_paddle(self, type):
        if type == 'ai':
            self.add_paddle(AI_STARTING_POSITION)
        else:
            self.add_paddle(PLAYER_STARTING_POSITION)

    def move_up(self):
        new_y = self.paddle_list[0].ycor() + MOVE_DISTANCE
        x = self.paddle_list[0].xcor()
        self.paddle_list[0].goto(x, new_y)

    def move_down(self):
        new_y = self.paddle_list[0].ycor() - MOVE_DISTANCE
        x = self.paddle_list[0].xcor()
        self.paddle_list[0].goto(x, new_y)


