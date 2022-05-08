import logging
import random
from flask import Flask


def make_h1(function):
    def wrapper_h1():
        return f"<h1>{function()}<h1>"
    return wrapper_h1


def gif_numbers(function):
    def wrapper_gif_numbers():
        return f"{function()}<br><img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"
    return wrapper_gif_numbers


def check_number(function):
    def wrapper_check_number(guess):
        if random_number < guess:
            return f"<h1 style='color: red'>Too high! Try again.</h1>" \
                   f"<br>" \
                   f"<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
        elif random_number > guess:
            return f"<h1 style='color: blue'>Too low! Try again.</h1>" \
                   f"<br>" \
                   f"<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
        else:
            return f"<h1 style='color: green'>You found me!</h1>" \
                   f"<br>" \
                   f"<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    return wrapper_check_number


app = Flask(__name__)


@app.route("/")
@make_h1
@gif_numbers
def higher_lower():
    return "Guess a number between 0 and 9"


@app.route("/<int:guess>")
@check_number
def game(guess):
    return f"random_number = {random_number}, guess = {guess}"


random_number = random.randint(0, 9)

if __name__ == "__main__":
    app.run(debug=True)
