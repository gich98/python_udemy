import requests
import smtplib
from flask import Flask, render_template, request
from post import Post

MY_EMAIL = "my@email.com"
MY_PASSWORD = "password."
YOUR_EMAIL = "your@email.com"
app = Flask(__name__)
all_posts = []


def get_posts():
    blog_endpoint = "https://api.npoint.io/198a953dd469b22df5a7"
    r = requests.get(url=blog_endpoint)
    posts = [Post(id=_["id"], title=_["title"], subtitle=_["subtitle"], body=_["body"],
                  date=_["date"], author=_["author"], image=_["image"]) for _ in r.json()]
    return posts


def send_email(name, email, phone, message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:New Message!\n\n"
                f"Name: {name}\n"
                f"Email: {email}\n"
                f"Phone: {phone}\n"
                f"Message: {message}"
        )


@app.route("/")
def get_home():
    global all_posts
    all_posts = get_posts()
    return render_template("index.html", all_posts=all_posts)


@app.route("/about")
def get_about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def get_contact():
    title_contact = "Contact Me"
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        title_contact = "Successfully sent your message"
    return render_template("contact.html", title=title_contact)


@app.route("/post/<id_post>")
def get_post(id_post):
    for _ in all_posts:
        print(f"{_.id} == {int(id_post)}? {_.id == int(id_post)}")
    post = [_ for _ in all_posts if _.id == int(id_post)]
    return render_template("post.html", post=post[0])


if __name__ == "__main__":
    app.run(debug=True)

# @app.route("/login", methods=["POST"])
# def get_login():
#     return render_template("login.html", name=request.form["name"], password=request.form["password"])

