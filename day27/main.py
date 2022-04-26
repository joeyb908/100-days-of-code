import tkinter

FONT = ("Arial", 10)

def calculate_miles_to_kilometers():
    """Take input, convert to kilometers, and print result"""
    miles = float(input.get())
    kilometers = miles * 1.609344
    kilometers_label.config(text=f"{kilometers:.2f}")

# create initial window and label it... add some padding to the top and bottom
window = tkinter.Tk()
window.title("Miles to Kilometer Calculator")
#window.minsize(width=100, height=0)
window.config(padx=5, pady=5)

# Label

# initial KM label
kilometers_label = tkinter.Label(text="0", font=FONT)
kilometers_label.grid(column=1, row=1)
kilometers_label.config(padx=5, pady=5)

# label that says "is equal to"
is_equal_txt = tkinter.Label(text="is equal to", font=FONT)
is_equal_txt.grid(column=0, row=1)

# label that simply says 'miles'
miles_txt = tkinter.Label(text="miles", font=FONT)
miles_txt.grid(column=2, row=0)
miles_txt.config(padx=2)

# label that simply says, 'kilometers'
km_txt = tkinter.Label(text="kilometers", font=FONT)
km_txt.grid(column=2, row=1)
km_txt.config(padx=2)
#
# button
# calculate button with function to calculate miles to km
calculate = tkinter.Button(text="Calculate", command=calculate_miles_to_kilometers)
calculate.grid(column=1, row=3)
#
# # entry
# entry field to take miles
input = tkinter.Entry(width=10)
input.grid(column=1, row=0)
input.get()

# required to run tkinter loop
window.mainloop()