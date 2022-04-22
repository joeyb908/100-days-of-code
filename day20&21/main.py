from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.tracer(0)

screen.bgcolor("black")
screen.title("Snake Game")

# create snake, food, and scoreboard classes
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()

# key actions to move snake
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    # display scoreboard and set screen to update once after every action completed
    scoreboard.display_score()
    screen.update()
    time.sleep(.1)
    snake.move()

    # randomize food location on screen, increase score, and extend body when eaten
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend_body()

    # end game when colliding into wall
    if snake.head.xcor() > 290 or snake.head.xcor() < - 300 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # end game when running into itself
    for body_piece in snake.snake_body[1:]:
        if snake.head.distance(body_piece) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
