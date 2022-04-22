from turtle import Turtle, Screen
from paddle import Paddle
from pong import Pong
import time
DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600

# set screen
screen = Screen()
screen.tracer(0)
screen.listen()
screen.setup(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
screen.bgcolor("black")

# create paddles and assign player/ai
player = Paddle('player')
ai = Paddle('ai')
ball = Pong()

# set keybinds
screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)


screen.exitonclick()