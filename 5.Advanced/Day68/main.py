from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
login_manager = LoginManager()
db = SQLAlchemy(app)
login_manager.init_app(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True)
    password = db.Column(db.String(250))
    name = db.Column(db.String(250))

    @staticmethod
    def is_active():
        return True

    @staticmethod
    def is_authenticated(self):
        return True

    @staticmethod
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id


# db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/")
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.form
        db_user = User.query.filter_by(email=data["email"]).first()
        if db_user and check_password_hash(db_user.password, data["password"]):
            login_user(db_user)
            return redirect(url_for("secrets", name=db_user.name))
        else:
            flash("Email doesn't exist or the Password is wrong!")
            return redirect(url_for("login", logged_in=current_user.is_authenticated))
    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        data = request.form
        db_user = User.query.filter_by(email=data["email"]).first()
        if db_user:
            flash("Email already exists!")
            return redirect(url_for("register"))
        hashed_password = generate_password_hash(password=data["password"], method="pbkdf2:sha256", salt_length=8)
        new_user = User(
            email=data["email"],
            password=hashed_password,
            name=data["name"],
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for("secrets", name=new_user.name))
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/secrets")
@login_required
def secrets():
    name = request.args.get('name')
    return render_template("secrets.html", name=name, logged_in=current_user.is_authenticated)


@app.route("/download")
@login_required
def download():
    return send_from_directory("static/files", "cheat_sheet.pdf", logged_in=current_user.is_authenticated)


if __name__ == "__main__":
    app.run(debug=True)
