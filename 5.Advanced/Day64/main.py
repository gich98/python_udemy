from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, InputRequired
from db import db
from movie import Movie
from movie_manager import MovieManager

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies-collection.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
Bootstrap(app)
db.init_app(app)
movie_manager = MovieManager(db, Movie)
movies = None


class RateMovieForm(FlaskForm):
    rating = FloatField(label="Your Rating Out of 10 e.g. 7.5", validators=[DataRequired(), InputRequired()])
    review = StringField(label="Your Review", validators=[DataRequired(), InputRequired()])
    done = SubmitField(label="Done")


class SearchMovieForm(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired(), InputRequired()])
    add = SubmitField(label="Search")


@app.route("/")
def home():
    global movies
    movies = movie_manager.get_all_movies()
    movies_sorted = sorted(movies, key=lambda a: a.ranking, reverse=True)
    return render_template("index.html", movies=movies_sorted)


@app.route("/edit/<movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    rate_movie_form = RateMovieForm()
    movie = movie_manager.get_movie_by_id(movie_id)
    if rate_movie_form.validate_on_submit():
        movie_manager.update_movie_rating(movie, rate_movie_form.rating.data, rate_movie_form.review.data)
        return redirect(url_for("home"))
    return render_template("edit.html", form=rate_movie_form, movie=movie)


@app.route("/delete/<movie_id>")
def delete(movie_id):
    movie_manager.delete_movie(movie_id)
    return redirect(url_for("home"))


@app.route("/search", methods=["GET", "POST"])
def search():
    search_movie_form = SearchMovieForm()
    if search_movie_form.validate_on_submit():
        movies_found = movie_manager.tmdb_search_movie(search_movie_form.title.data)
        return render_template("list_movies.html", movies=movies_found)
    return render_template("search.html", form=search_movie_form)


@app.route("/select/<movie_id>")
def select(movie_id):
    movie = movie_manager.tmdb_movie_details(movie_id)
    return render_template("select.html", movie=movie)


@app.route("/add/<movie_id>")
def add(movie_id):
    # TODO check number of movies in the list, max 10 movies
    # if len(movie_manager.get_all_movies()) < 10:
    movie_manager.add_movie(movie_id)
    return redirect(url_for("edit", movie_id=movie_id))


if __name__ == '__main__':
    app.run(debug=True)
