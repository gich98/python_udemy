import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

SECRET_API_KEY = "SuperSecretApiKey"
app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def __repr__(self):
        return "Cafe infos:\n" \
               f"- ID -> {self.id}\n" \
               f"- Name -> {self.name}\n" \
               f"- Map URL -> {self.map_url}\n" \
               f"- Img URL -> {self.img_url}\n" \
               f"- Location -> {self.location}\n" \
               f"- Seats -> {self.seats}\n" \
               f"- Toilet -> {self.has_toilet}\n" \
               f"- Wifi -> {self.has_wifi}\n" \
               f"- Sockets -> {self.has_sockets}\n" \
               f"- Calls -> {self.can_take_calls}\n" \
               f"- Coffee Price -> {self.coffee_price}\n"

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record

@app.route("/random")
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all")
def get_all_cafes():
    cafes = db.session.query(Cafe).all()
    cafes_dict = [cafe.to_dict() for cafe in cafes]
    return jsonify(cafes=cafes_dict)


@app.route("/search")
def get_cafe_by_location():
    query_location = request.args.get("loc")
    cafe = db.session.query(Cafe).filter_by(location=query_location).first()
    if cafe:
        return jsonify(cafe=cafe.to_dict())
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(request.form.get("has_sockets")),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )

    api_key = request.args.get("api-key")
    if api_key == SECRET_API_KEY:
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(response={"success": f"Successfully added the new cafe"}), 200
    else:
        return jsonify(error={"Forbidden": "Sorry, the api_key is not correct."}), 403


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def patch_update_price_by_id(cafe_id):
    new_price = request.args.get("new_price")
    api_key = request.args.get("api-key")
    if api_key == SECRET_API_KEY:
        cafe = Cafe.query.get(cafe_id)
        if cafe:
            cafe.coffee_price = new_price
            db.session.commit()
            return jsonify(response={"success": f"Successfully updated the cafe with id {cafe_id}"}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error={"Forbidden": "Sorry, the api_key is not correct."}), 403


# HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == SECRET_API_KEY:
        cafe = Cafe.query.get(cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": f"Successfully deleted the cafe with id {cafe_id}"}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error={"Forbidden": "Sorry, the api_key is not correct."}), 403


if __name__ == '__main__':
    app.run(debug=True)
