from tkinter import *


def button_clicked():
    label["text"] = user_input.get()


# Tkinter Layout Manager: pack(), place() and grid()

# Window
window = Tk()
window.title("My first Python GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
label = Label(text="I am a Label", font=("Arial", 24, "bold"))
label.config(text="New text")
label.grid(column=0, row=0)

# Button
button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)
new_button = Button(text="New Click me", command=button_clicked)
new_button.grid(column=2, row=0)

# Entry
user_input = Entry(width=10)
user_input.grid(column=3, row=2)

window.mainloop()
