import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import threading

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager(player)
scoreboard = Scoreboard()

screen.onkeypress(player.up, "Up")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.01)

    car_manager.car_scheduler(player)
    player.player_rules()

    if player.ycor() >= 260:
        scoreboard.increase_level()

    for car in car_manager.car_list:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()