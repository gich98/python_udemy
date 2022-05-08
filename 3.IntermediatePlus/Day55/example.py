from flask import Flask


def make_bold(function):
    def wrapper_bold():
        return "<b>" + function() + "</b>"
    return wrapper_bold


def make_emphasis(function):
    def wrapper_emphasis():
        return "<em>" + function() + "</em>"
    return wrapper_emphasis


def make_underlined(function):
    def wrapper_underlined():
        return "<u>" + function() + "</u>"
    return wrapper_underlined


app = Flask(__name__)


@app.route('/')
@make_bold
@make_underlined
@make_emphasis
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph</p>'


@app.route("/bye")
def say_bye():
    return "Bye"


@app.route("/hello/<username>")
def greet(username):
    return f"Hello {username}!"


if __name__ == "__main__":
    app.run(debug=True)
