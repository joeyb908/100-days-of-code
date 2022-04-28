from tkinter import *
import pandas
import random
timer = None

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Arial"
COUNT = 3


def select_random_word():
    """Select a random French word & accompanying English word"""
    word_data = pandas.read_csv("./data/french_words.csv")
    word_data = word_data.to_dict()

    # choose a random index, then return the word for the language chosen
    random_index = random.randint(0, 100)
    return [word_data["French"][random_index], word_data["English"][random_index]]


def count_down(count, language, french_word, english_word):
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1, language, french_word, english_word)
    else:
        canvas.itemconfig(canvas_image, image=card_back_img)
        canvas.itemconfig(language_text, text=f"{language}", fill="white")
        canvas.itemconfig(word_text, text=f"{english_word}", fill="white", font=(FONT, 60, "bold"))


def new_word():
    random_word = select_random_word()

    french_word = random_word[0]
    english_word = random_word[1]

    canvas.itemconfig(word_text, text=f"{french_word}", fill="black", font=(FONT, 60, "bold"))
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(canvas_image, image=card_front_img)

    count_down(COUNT, 'English', french_word, english_word)


# initial window
window = Tk()
window.minsize(height=556, width=800)
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# create initial canvas with card front
canvas = Canvas(height=556, width=800)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 278, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
language_text = canvas.create_text(400, 150, text="Ready to start?", font=(FONT, 40, "italic"))
word_text = canvas.create_text(400, 330, text="Click either the red X or the green ✔ to get started!",
                               font=(FONT, 20, "bold"))


# buttons
wrong_button_img = PhotoImage(file="./images/wrong.png")
right_button_img = PhotoImage(file="./images/right.png")

wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=new_word)
wrong_button.grid(column=0, row=1)

right_button = Button(image=right_button_img, highlightthickness=0, command=new_word)
right_button.grid(column=1, row=1)


# used canvas instead of labels
# labels
# language_label = Label(text="French", font=(FONT, 40, "italic"), bg="white")
# language_label.place(x=300, y=150)

# word_label = Label(text="word", font=(FONT, 60, "bold"), bg="white")
# word_label.place(x=300, y=263)

#english_french_word = select_random_word()


mainloop()