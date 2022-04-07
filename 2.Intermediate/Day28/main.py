import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
    elif reps == 8:
        timer_label.config(text="Long Break", fg=RED)
        count_down(long_break_sec)
    else:
        timer_label.config(text="Short Break", fg=PINK)
        count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minute = math.floor(count / 60)
    seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{minute:02}:{seconds:02}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    elif reps < 8:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps / 2)):
            mark += "✔"
        checkmark_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=150, pady=50, bg=YELLOW)
window.minsize(width=600, height=400)

image = PhotoImage(file="tomato.png")
canvas = Canvas(width=202, height=226, bg=YELLOW, highlightthickness=0)
timer_label = Label(text="Timer", font=(FONT_NAME, 32, "bold"), bg=YELLOW)
checkmark_label = Label(font=(FONT_NAME, 15, "normal"), bg=YELLOW)
start_button = Button(text="Start", highlightthickness=0, width=8, height=1, command=start_timer)
reset_button = Button(text="Reset", highlightthickness=0, width=8, height=1, command=reset_timer)

canvas.create_image(102, 114, image=image)
timer_text = canvas.create_text(102, 130, text="25:00", fill="white", font=(FONT_NAME, 28, "bold"))

timer_label.grid(column=1, row=0)
canvas.grid(column=1, row=1)
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)
checkmark_label.grid(column=1, row=3)

window.mainloop()
