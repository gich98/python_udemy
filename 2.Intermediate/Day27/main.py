from tkinter import *


def convert_miles_to_km():
    miles_value = int(miles_entry.get())
    km_value = round(miles_value * 1.609)
    km_value_label.config(text=f"{km_value}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=30, pady=20)

miles_entry = Entry(width=10)
miles_label = Label(text="Miles")
is_equals_to_label = Label(text="is equal to")
km_value_label = Label(text="0")
km_label = Label(text="Km")
calculate_button = Button(text="Calculate", command=convert_miles_to_km)


miles_entry.grid(column=1, row=0)
miles_label.grid(column=2, row=0)
is_equals_to_label.grid(column=0, row=1)
km_value_label.grid(column=1, row=1)
km_label.grid(column=2, row=1)
calculate_button.grid(column=1, row=2)

window.mainloop()
