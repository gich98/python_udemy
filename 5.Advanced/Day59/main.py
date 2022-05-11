from pprint import pprint

from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)
all_posts = []


def get_posts():
    blog_endpoint = "https://api.npoint.io/198a953dd469b22df5a7"
    r = requests.get(url=blog_endpoint)
    posts = [Post(id=_["id"], title=_["title"], subtitle=_["subtitle"], body=_["body"],
                  date=_["date"], author=_["author"], image=_["image"]) for _ in r.json()]
    return posts


@app.route("/")
def get_home():
    global all_posts
    all_posts = get_posts()
    return render_template("index.html", all_posts=all_posts)


@app.route("/about")
def get_about():
    return render_template("about.html")


@app.route("/contact")
def get_contact():
    return render_template("contact.html")


@app.route("/post/<id_post>")
def get_post(id_post):
    for _ in all_posts:
        print(f"{_.id} == {int(id_post)}? {_.id == int(id_post)}")
    post = [_ for _ in all_posts if _.id == int(id_post)]
    return render_template("post.html", post=post[0])


if __name__ == "__main__":
    app.run(debug=True)
