from turtle import Turtle
direction_vector = [-3, -3]
BALL_SPEED = 3


class Pong(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed("fastest")
        self.penup()
        self.color("white")
        self.goto(0, 0)

    def move(self, player, ai):
        self.goto(self.xcor() + direction_vector[0], self.ycor() + direction_vector[1])
        self.bounce_walls()
        self.paddle_collision(player, ai)

    def bounce_walls(self):
        if self.ycor() >= 290:
            diff = self.ycor() - 290
            direction_vector[1] *= -1
            self.goto(self.xcor() + direction_vector[0], self.ycor() - diff)
        elif self.ycor() <= - 290:
            diff = - 290 - self.ycor()
            direction_vector[1] *= -1
            self.goto(self.xcor() + direction_vector[0], self.ycor() + diff)

    def paddle_collision(self, player, ai):
        if self.xcor() >= 340 and self.distance(ai) <= 30:
            diff = self.xcor() - 340
            direction_vector[0] *= -1
            self.goto(self.xcor() + (direction_vector[0]) - diff, self.ycor())

        if self.xcor() <= -340 and self.distance(player) <= 30:
            diff = -340 - self.xcor()  # positive diff
            direction_vector[0] *= -1
            self.goto(self.xcor() + (direction_vector[0]) + diff, self.ycor())

    def game_over(self):
        if self.xcor() < - 420 or self.xcor() > 420:
            return True
        else:
            return False

    def bounce_x(self):
        direction_vector[0] *= -1

    def reset(self):
        self.goto(0, 0)

    # my method

    # def bounce_off_walls(self):
    #     if (self.ball.ycor() < - 290 or self.ball.ycor() > 290) and self.ball.heading() == 45:
    #         self.ball.setheading(315)
    #
    #     elif (self.ball.ycor() < - 290 or self.ball.ycor() > 290) and self.ball.heading() == 225:
    #         self.ball.setheading(135)
    #
    #     elif (self.ball.ycor() < - 290 or self.ball.ycor() > 290) and self.ball.heading() == 135:
    #         self.ball.setheading(225)
    #
    #     elif (self.ball.ycor() < - 290 or self.ball.ycor() > 290) and self.ball.heading() == 315:
    #         self.ball.setheading(45)
    #
    # def collision_with_wall(self, game_state):
    #     if self.ball.xcor() < - 400 or self.ball.xcor() > 400:
    #         game_state = False
    #         return game_state
    #     else:
    #         return True
    #
    # def bounce_off_paddles(self, player_paddle, ai_paddle):
    #     if (self.ball.distance(player_paddle) < 15 or self.ball.distance(ai_paddle) < 15) and self.ball.heading() == 45:
    #         self.ball.setheading(135)
    #
    #     elif (self.ball.distance(player_paddle) < 15 or self.ball.distance(ai_paddle) < 15) and self.ball.heading() == 225:
    #         self.ball.setheading(315)
    #
    #     elif (self.ball.distance(player_paddle) < 15 or self.ball.distance(ai_paddle) < 15) and self.ball.heading() == 135:
    #         self.ball.setheading(45)
    #
    #     elif (self.ball.distance(player_paddle) < 15 or self.ball.distance(ai_paddle) < 15) and self.ball.heading() == 315:
    #         self.ball.setheading(225)

