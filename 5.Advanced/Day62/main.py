from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, SelectField, TimeField
from wtforms.validators import InputRequired, URL
from flask_bootstrap import Bootstrap
from manager_cafes import ManagerCafes
from cafe import Cafe


class CafeForm(FlaskForm):
    name_cafe = StringField(label="Cafe Name", validators=[InputRequired()])
    location = URLField(label="Cafe Location on Google Maps (URL)", validators=[InputRequired(), URL()])
    open_cafe = TimeField(label="Open", validators=[InputRequired()])
    close_cafe = TimeField(label="Close", validators=[InputRequired()])
    coffee = SelectField(u'Coffee Rating', choices=["☕", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"])
    wifi = SelectField(u'Wifi Strength Rating', choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"])
    power = SelectField(u'Power Socket Availability', choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"])
    submit = SubmitField(label="Submit")


manager_cafes = ManagerCafes()
app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/cafes")
def get_cafes():
    return render_template("cafes.html", cafes=manager_cafes.cafes)


@app.route("/add", methods=["GET", "POST"])
def add():
    cafe_form = CafeForm()
    if cafe_form.validate_on_submit():
        manager_cafes.add_cafe(Cafe(
            name=cafe_form.name_cafe.data,
            location=cafe_form.location.data,
            open_cafe=cafe_form.open_cafe.data.strftime("%I:%M %p"),
            close_cafe=cafe_form.close_cafe.data.strftime("%I:%M %p"),
            coffee=cafe_form.coffee.data,
            wifi=cafe_form.wifi.data,
            power=cafe_form.power.data
        ))
    return render_template("add.html", form=cafe_form)


if __name__ == "__main__":
    app.run(debug=True)
