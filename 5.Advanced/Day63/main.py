from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import InputRequired, NumberRange
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)
db = SQLAlchemy(app)
all_books = []
db.create_all()


class BookDB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Title %r>' % self.title


class BookForm(FlaskForm):
    name = StringField(label="Book Name", validators=[InputRequired()])
    author = StringField(label="Book Author", validators=[InputRequired()])
    rating = FloatField(label="Rating", validators=[InputRequired(), NumberRange(min=0, max=10)])
    add_book = SubmitField(label="Add Book")


class BookUpdateRatingForm(FlaskForm):
    rating = FloatField(label="Rating", validators=[InputRequired(), NumberRange(min=0, max=10)])
    update_rating = SubmitField(label="Update Rating")


@app.route('/')
def home():
    global all_books
    all_books = db.session.query(BookDB).all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    book_form = BookForm()
    if book_form.validate_on_submit():
        db.session.add(BookDB(title=book_form.name.data, author=book_form.author.data, rating=book_form.rating.data))
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html", form=book_form)


@app.route("/edit/<book_id>", methods=["GET", "POST"])
def edit(book_id):
    book_update_rating_form = BookUpdateRatingForm()
    book_to_update = BookDB.query.get(book_id)
    if book_update_rating_form.validate_on_submit():
        book_to_update.rating = book_update_rating_form.rating.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form=book_update_rating_form, book=book_to_update)


@app.route("/delete/<book_id>")
def delete(book_id):
    book_to_delete = BookDB.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

