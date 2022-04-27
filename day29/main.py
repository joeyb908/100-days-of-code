from tkinter import *
from tkinter import messagebox
import random
import pyperclip


FONT = ("Cambria", 12)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    """Generates a randomize password of length 12 - 18"""

    # list containing all letters, symbols, and numbers commonly used in English keyboard
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # randomly generate the number of letters, symbols, and numbers that are going to be used
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # empty password list
    password_list = []

    # append a random letter to the list in the range of randomly generated range of letters
    [password_list.append(random.choice(letters)) for char in range(nr_letters)]
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    # append a random symbol to the list in the range of randomly generated range of symbols
    [password_list.append(random.choice(symbols)) for symbol in range(nr_symbols)]
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    # append a random number to the list in the range of randomly generated range of numbers
    [password_list.append(random.choice(numbers)) for number in range(nr_numbers)]
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    # shuffle the password list so the password isn't presented in the form of:
    # letters, symbols, numbers
    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #     password += char
    # join the characters in the password list with nothing inbetween
    password = "".join(password_list)

    # delete currently placed password and replace with randomly generated password
    pass_entry.delete(0, END)
    pass_entry.insert(0, password)

    # copy password to clipboard
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    """Save data to a file, 'data.txt'"""

    # get website, username, and pass input
    website = website_entry.get()
    username = username_entry.get()
    password = pass_entry.get()

    # if the website or password is empty or if both are empty, generate popup box that lets the user know
    # that something is missing
    if (len(website) or len(password)) == 0 or (len(website) and len(password)) == 0:
        messagebox._show(title="Field Empty", message="You left either the website or password blank!")

    # otherwise, popup and ok/cancel box. if okay is clicked, continue
    else:
        is_okay = messagebox.askokcancel(title=website, message=f"These are the details entered:\n"
                                                      f"Email: {website}\n"
                                                      f"Username: {username}\n"
                                                      f"Password: {password}\n"
                                                      f"Is it okay to save?")

        # if details are okay, append the data to a new text file
        if is_okay:
            # open data.txt, if doesn't exist, creates and appends to end
            with open("data.txt", "a") as data:
                data.write(f"{website}, {username}, {password}\n")

            # clears website and password fields
            clear_fields()


def clear_fields():
    """Clears website and password fields"""

    website_entry.delete(0, END)
    pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# create initial window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# create image
canvas = Canvas(height=200, width=200)
pwd_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pwd_img)
canvas.grid(column=1, row=0)

# create website label and right align
website_label = Label(text="Website", font=FONT)
website_label.grid(column=0, row=1, sticky="E")

# create username label and right align
email_username_label = Label(text="Email/Username", font=FONT)
email_username_label.grid(column=0, row=2, sticky="E")

# create password label and right aligh
password_label = Label(text="Password:", font=FONT)
password_label.grid(column=0, row=3, sticky="E")

# create website entry and left/right align
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")

# create username entry and left/right align
username_entry = Entry(width=35)
username_entry.insert(0, string="joeyb908@gmail.com")
username_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

# create passgen entry and left/right align
pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=3, sticky="EW")

# create generate button
generate_pass_button = Button(text="Generate Password", font=FONT, command=generate_password)
generate_pass_button.grid(column=2, row=3)

# create add button and left/right  align
add_button = Button(text="Add", font=FONT, width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")


window.mainloop()