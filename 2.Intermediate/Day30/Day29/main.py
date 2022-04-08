from tkinter import *  # from module import *, imports only the Classes and Constants
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- SEARCH CREDENTIALS ------------------------------- #
def search_credential():
    website_content = website_entry.get()
    if website_content != "":
        try:
            with open(file="data.json", mode="r") as file:
                data = json.load(file)
                email = data[website_content]["email"]
                password = data[website_content]["password"]
        except (FileNotFoundError, json.decoder.JSONDecodeError, KeyError):
            open(file="data.json", mode="w")
            messagebox.showwarning(title="Oops", message=f"You don't have any credentials for {website_content}.")
        else:
            messagebox.showinfo(title=f"Credentials for {website_content}",
                                message=f"Email/Username: {email}\nPassword: {password}")
    else:
        messagebox.showerror(title="Oops", message="Enter the Website you want to search for")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)] \
                    + [random.choice(symbols) for _ in range(nr_symbols)] \
                    + [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    password_entry.delete(0, END)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_content = website_entry.get()
    email_username_content = email_username_entry.get()
    password_content = password_entry.get()
    new_data = {
        website_content: {
            "email": email_username_content,
            "password": password_content,
        }
    }

    if (website_content != "") and (email_username_content != "") and (password_content != ""):
        try:
            with open(file="data.json", mode="r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            data = new_data
        else:
            data.update(new_data)
        with open(file="data.json", mode="w") as file:
            json.dump(data, file, indent=4)
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    else:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
website_label = Label(text="Website:")
email_username_label = Label(text="Email/Username:")
password_label = Label(text="Password:")
website_entry = Entry(width=33)
email_username_entry = Entry(width=52)
password_entry = Entry(width=33)
generate_password_button = Button(text="Generate Password", command=generate_password)
add_button = Button(text="Add", width=44, command=save)
search_button = Button(text="Search", width=14, command=search_credential)

canvas.grid(row=0, column=1)
website_label.grid(row=1, column=0)
website_entry.grid(row=1, column=1)
search_button.grid(row=1, column=2)
email_username_label.grid(row=2, column=0)
email_username_entry.grid(row=2, column=1, columnspan=2)
password_label.grid(row=3, column=0)
password_entry.grid(row=3, column=1)
generate_password_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2)

canvas.create_image(100, 100, image=image)
website_entry.focus()
email_username_entry.insert(0, "username@email.com")

window.mainloop()
