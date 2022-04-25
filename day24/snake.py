from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
        self.caboose = self.snake_body[-1]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_body(position)

    def add_body(self, position):
        new_snake_body = Turtle(shape="square")
        new_snake_body.color("white")
        new_snake_body.penup()
        new_snake_body.goto(position)
        new_snake_body.speed("fastest")
        self.snake_body.append(new_snake_body)

    def extend_body(self):
        self.add_body(self.caboose.position())

    def move(self):
        # move snake forward from the back up
        for index in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[index - 1].xcor()
            new_y = self.snake_body[index - 1].ycor()
            self.snake_body[index].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for piece in self.snake_body:
            piece.goto(1000,1000)
        self.snake_body.clear()
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
        self.caboose = self.snake_body[-1]
