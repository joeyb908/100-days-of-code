from turtle import Turtle, Screen
import random as r


def randomize_color(COLORS):
    """Extremely convoluted way of just going through a list and making sure I didn't repeat a value"""
    # could have just done this
    # for color_index in range(0,7):
    #   turtle.color(COLORS[color])
    color = r.choice(COLORS)
    COLORS.remove(color)
    return color
# upon reviewing the index solution code more, I like my solution more because
# the turtle colors are randomized and not just the same over and over


COLORS = ["red", "orange", "green", "blue", "indigo", "violet"]
TURTLE_NAMES = ["tom", "kim", "ben", "mike", "elle", "tim"]
all_turtles = []

TURTLE_SIZE = 40
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
screen.colormode(255)

user_bet = screen.textinput("Place a Bet", "Which turtle do you think will win?\n"
                                           "Available colors are from the rainbow (minus yellow).\nROGBIV").lower()


# Set turtle positions to the same y value but space them out 40 pixels...
# also randomize the turtle color
screen_x = int((screen.window_width() * -1) / 2 + 40)
screen_y = int((screen.window_height() * -1) / 2 / 2)
for turtle in TURTLE_NAMES:
    turtle = Turtle(shape="turtle")
    turtle.color(randomize_color(COLORS))
    turtle.penup()
    turtle.goto(screen_x, screen_y)
    screen_y += 40
    all_turtles.append(turtle)


# keeps the loop from starting before bets are placed
if user_bet:
    is_race_on = True

while is_race_on:
    # each turtle randomly moves forward
    for turtle in all_turtles:
        rand_distance = r.randint(0, 10)
        turtle.forward(rand_distance)
        x = turtle.xcor()
        # when the turtle reaches the end of the screen, end the race
        if x > screen.window_width() / 2 - TURTLE_SIZE/2:
            if user_bet == turtle:
                print(f"You win! {turtle.color()[0].title()} turtle finished in 1st!")
                is_race_on = False
            else:
                print(f"You loser! Guess better next time. The {turtle.color()[0].title()} turtle won.")
                is_race_on = False


screen.exitonclick()
