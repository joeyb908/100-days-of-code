from tkinter import *
import math
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 15
SEC_IN_MIN = 60
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 10
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    # stop the timer
    window.after_cancel(timer)

    #reset the check marks
    check = []
    check_marks.config(text=check)

    # reset the top label
    timer_label.config(text="Timer", font=(FONT_NAME, 40))
    canvas.itemconfig(timer_text, text=f"00:00")

    # reset reps to 0
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    """Start the countdown"""
    # increase reps by 1
    global reps
    reps += 1

    # convert work and break minutes to seconds
    work_sec = int(WORK_MIN * SEC_IN_MIN)
    short_break_sec = int(SHORT_BREAK_MIN * SEC_IN_MIN)
    long_break_sec = int(LONG_BREAK_MIN * SEC_IN_MIN)

    # if set of 8, long break
    # if set of 2, short break
    # if none, continue the timer
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED, font=(FONT_NAME, 40, "bold"))
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK, font=(FONT_NAME, 40, "bold"))
    else:
        count_down(work_sec)
        timer_label.config(text="Work", font=(FONT_NAME, 40, "bold"))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    """Convert seconds to minutes & seconds, count down every 1000 ms (1 second)"""

    global reps
    # get minutes and seconds
    count_minutes = math.floor(count / SEC_IN_MIN)
    count_seconds = count % SEC_IN_MIN

    # if the count is less than 10 seconds, stick a 0 in front then add the number so it reads like this: 3:03 instead
    # of 3:3 for the time left
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    # change the timer text to represent minutes and seconds left
    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")

    # count down to 0 every second then stop
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            check.append("✔")
            check_marks.config(text=check)


# ---------------------------- UI SETUP ------------------------------- #
# create initial tkinter window
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# create timer label at top
timer_label = Label(text="Timer", font=(FONT_NAME, 40), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

# create canvas and add tomato image on top
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# create start bottom
start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

# create reset button
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=3, row=2)

# create an empty list of check marks, then apply to the label
check = []
check_marks = Label(text=check, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
check_marks.grid(column=1, row=3)

# main loop for window to stay on screen
window.mainloop()












