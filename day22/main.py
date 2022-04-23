from turtle import Screen
from paddle import Paddle
from pong import Pong
from scoreboard import Scoreboard
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
player = Paddle((-370, 0))
ai = Paddle((370, 0))
scoreboard = Scoreboard()
scoreboard.display_score()
game_line = Scoreboard()
ball = Pong()

# set keybinds
screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_down, "Down")
screen.onkeypress(ai.move_up, "w")
screen.onkeypress(ai.move_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed())
    ball.move(player, ai)

    reset = ball.game_over()

    if reset:
        if ball.xcor() < 0:
            scoreboard.increase_ai_score()
        else:
            scoreboard.increase_player_score()
        ball.bounce_x()
        ball.reset()


    #game_is_on = ball.bounce_off_walls(game_is_on)
    #ball.bounce_off_paddles(player.paddle_list[0], ai.paddle_list[0])


screen.exitonclick()