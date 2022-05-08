import datetime
import requests
import json
from flask import Flask, render_template


app = Flask(__name__)


def genderize(name):
    genderize_endpoint = "https://api.genderize.io"
    params = {
        "name": name,
        "country_id": "IT"
    }
    r = requests.get(url=genderize_endpoint, params=params)
    return r.json()["gender"]


def agify(name):
    agify_endpoint = "https://api.agify.io"
    params = {
        "name": name,
    }
    r = requests.get(url=agify_endpoint, params=params)
    return r.json()["age"]


@app.route("/")
def home():
    year = datetime.datetime.today().year
    author = "VKind"
    return render_template("example2.html", year=year, author=author)


@app.route("/guess/<name>")
def guess(name):
    year = datetime.datetime.today().year
    author = "VKind"
    guess_age = agify(name)
    guess_gender = genderize(name)
    return render_template("guess.html", year=year, author=author, gender=guess_gender, age=guess_age, name=name)


@app.route("/blog")
def get_blog():
    blog_endpoint = "https://api.npoint.io/c790b4d5cab58020d391"
    r = requests.get(url=blog_endpoint)
    all_posts = r.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
