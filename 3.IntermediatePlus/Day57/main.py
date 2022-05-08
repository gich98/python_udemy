import requests
import json
from flask import Flask, render_template
from post import Post

app = Flask(__name__)
all_posts = []


def get_posts():
    blog_endpoint = "https://api.npoint.io/c790b4d5cab58020d391"
    r = requests.get(url=blog_endpoint)
    posts = [Post(id=_["id"], title=_["title"], subtitle=_["subtitle"], body=_["body"]) for _ in r.json()]
    return posts


@app.route('/')
def home():
    global all_posts
    all_posts = get_posts()
    return render_template("index.html", all_posts=all_posts)


@app.route('/blog/<id_post>')
def get_blog(id_post):
    post = [_ for _ in all_posts if _.id == int(id_post)]
    return render_template("post.html", title=post[0].title, subtitle=post[0].subtitle, body=post[0].body)


if __name__ == "__main__":
    app.run(debug=True)
