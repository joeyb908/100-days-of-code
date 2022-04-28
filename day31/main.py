from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Arial"

# initial window
window = Tk()
window.minsize(height=556, width=800)
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# create initial canvas with card front
canvas = Canvas(height=556, width=800)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
canvas.create_image(400, 278, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)


# buttons
wrong_button_img = PhotoImage(file="./images/wrong.png")
right_button_img = PhotoImage(file="./images/right.png")

wrong_button = Button(image=wrong_button_img, highlightthickness=0)
wrong_button.grid(column=0, row=1)

right_button = Button(image=right_button_img, highlightthickness=0)
right_button.grid(column=1, row=1)

# labels
language_label = Label(text="Language", font=(FONT, 40, "italic"), bg="white")
language_label.place(x=300, y=150)

word_label = Label(text="word", font=(FONT, 60, "bold"), bg="white")
word_label.place(x=300, y=263)

mainloop()