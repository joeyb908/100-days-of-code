from turtle import Turtle, Screen
import random as r

COLOR_LIST = [
    (210, 156, 102), (57, 98, 133), (157, 81, 52), (138, 159, 192), (51, 174, 121), (232, 201, 101), (158, 167, 39),
    (121, 190, 175), (202, 135, 153), (66, 39, 33), (75, 113, 88), (26, 48, 67), (133, 29, 48), (127, 81, 91),
    (181, 93, 109), (197, 93, 74), (117, 37, 24), (5, 68, 50), (56, 31, 45), (231, 203, 0), (74, 132, 199),
    (161, 191, 224), (31, 65, 105), (26, 164, 170), (16, 84, 56), (149, 210, 192)
]
STARTING_POSITION = (-400, -300)

# default values for tim the Turtle
tim = Turtle()
tim.shape("turtle")
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setposition(STARTING_POSITION)
screen = Screen()
screen.colormode(255)

# utilized color gram to get initial set of colors from image.jpg
# import colorgram
#
# extracted_colors = colorgram.extract("image.jpg", 30)
# rgb_colors = []
#
# for color in extracted_colors:
#     rgb = color.rgb
#     red = rgb.r
#     green = rgb.g
#     blue = rgb.b
#     rgb = (red, green, blue)
#
#     rgb_colors.append(rgb)


def randomize_color(COLOR_LIST):
    """Randomize color each call"""
    return r.choice(COLOR_LIST)


def dashed_forward_line(COLOR_LIST):
    """Draw dots of size 20 spaced by 50 pixels"""
    for i in range(10):
        tim.dot(20, r.choice(COLOR_LIST))
        tim.setheading(0)
        tim.forward(50)


def return_one_line_up():
    """Return at same x value at start by 50 pixels higher"""
    tim.goto(STARTING_POSITION[0], tim.position()[1] + 50)


for i in range(10):
    dashed_forward_line(COLOR_LIST)
    return_one_line_up()

screen.exitonclick()
