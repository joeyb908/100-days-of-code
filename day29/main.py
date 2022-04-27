from tkinter import *
FONT = ("Cambria", 12)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")

# create username entry and left/right align
username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

# create passgen entry and left/right align
pass_gen = Entry(width=21)
pass_gen.grid(column=1, row=3, sticky="EW")

# create generate button
generate_pass_button = Button(text="Generate Password", font=FONT)
generate_pass_button.grid(column=2, row=3)

# create add button and left/right  align
add_button = Button(text="Add", font=FONT, width=35)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")


window.mainloop()