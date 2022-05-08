import datetime
import random
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    year = datetime.datetime.today().year
    author = "VKind"
    return render_template("example.html", num=random_number, year=year, author=author)


if __name__ == "__main__":
    app.run(debug=True)
