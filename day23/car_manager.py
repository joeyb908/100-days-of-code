from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2
FINISH_LINE = 280
STARTING_CAR_SPEED = 25


class CarManager(Turtle):
    def __init__(self, player):
        super().__init__()
        self.car_list = []
        self.car_speed = STARTING_CAR_SPEED
        self.player = player

    def car_scheduler(self, player):
        self.hideturtle()
        if random.randint(1,self.car_speed) == 1:
            self.create_car()
        self.move_cars()
        self.increase_speed(player)

    def move_cars(self):
        for car in self.car_list:
            car.goto(car.xcor() - MOVE_INCREMENT, car.ycor())


    def create_car(self):
        new_car = Turtle(shape="square")
        new_car.shapesize(stretch_wid=1, stretch_len=2.5)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.goto(320, random.randint(-250, 250))
        new_car.speed("fastest")
        self.car_list.append(new_car)

    def increase_speed(self, player):
        if player.ycor() > 270:
            self.car_speed -= 2


