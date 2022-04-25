import turtle
import pandas

# initialize screen with blank states map
screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

# initialize the write to map ability
state_writing = turtle.Turtle()
state_writing.penup()
state_writing.hideturtle()

# open 50_states.csv and save the data as a dictionary
with open("50_states.csv") as data:
    data = pandas.read_csv("50_states.csv")
    data_dict = data.to_dict()

all_states = data.state.to_list()

# get the state entered and save it
answer_state = screen.textinput("Guess the State", "What's a state's name?").title()

#initial settings for game loop, score, and x,y coords
guessing = True
score = 0
x = ''
y = ''

guessed_states = []
while guessing:

    # for each value in the state dictionary
    # if the guess equals the state
    # increase score by one
    # send the state to the coordinates on the map
    # for state in data_dict["state"]:
    #     if answer_state == data_dict["state"][state]:
    #         state_name = data_dict["state"][state]
    #         score += 1
    #         x = data_dict["x"][state]
    #         y = data_dict["y"][state]
    #         st_coordinates = (x, y)
    #         state_writing.goto(st_coordinates)
    #         state_writing.write(f"{state_name}", align="center")

    # teacher solution
    # utilizes pandas more
    # if answer is in the all_states list
    # get the row of data for the state
    # send the writing to the x and y value stored
    # write it out
    if answer_state in all_states:
        chosen_state = data[data.state == answer_state]
        state_writing.goto(int(chosen_state.x), int(chosen_state.y))
        state_writing.write(f"{answer_state}", align="center")
        score += 1
        guessed_states.append(answer_state)

    if len(guessed_states) == len(all_states):
        guessing = False

    # get new input for the mainloop
    answer_state = screen.textinput(f"Guess the State {score}/50", "What's a state's name?\nType exit to "
                                                                   "quit and see your results.").title()
    if answer_state == "Exit":
        missed_states = []
        for state in all_states:
            if state not in guessed_states:
                missed_states.append(state)
        missed_st = pandas.DataFrame(missed_states, columns=["state"])
        missed_st.to_csv("missed_states.csv")
        guessing = False
        # missed_df.to_csv("missed_states.csv")



screen.exitonclick()