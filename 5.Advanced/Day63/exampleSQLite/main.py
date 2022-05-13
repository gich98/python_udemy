import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Title %r>' % self.title


db.create_all()

book_1 = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=7.8)
book_2 = Book(id=2, title="22 SECONDS", author="James Patterson and Maxine Paetrog", rating=8)
book_3 = Book(title="It ends with us", author="Colleen Hoover", rating=5.3)
db.session.add(book_1)
db.session.add(book_2)
db.session.add(book_3)
db.session.commit()

# Read all records
all_books = db.session.query(Book).all()

# Read a particular record
book = Book.query.filter_by(title="Harry Potter").first()

# Update a particular record by query
book_to_update = Book.query.filter_by(title="Harry Potter").first()
book_to_update.title = "Harry Potter and the Chamber of Secrets"
db.session.commit()

# Update a particular record by ID
book_id = 1
book_to_update = Book.query.get(book_id)
book_to_update.title = "Harry Potter and the Goblet of Fire"
db.session.commit()

# Delete a particular record by ID
book_title = "Harry Potter and the Goblet of Fire"
book_to_delete = Book.query.filter_by(title=book_title).first()
db.session.delete(book_to_delete)
db.session.commit()

# Delete a particular record by ID
book_id = 1
book_to_delete = Book.query.get(book_id)
db.session.delete(book_to_delete)
db.session.commit()


# db = sqlite3.connect("new-books-collection.db")
# cursor = db.cursor()
# cursor.execute(
#     "CREATE TABLE books ("
#     "id INTEGER PRIMARY KEY, "
#     "title varchar(250) NOT NULL UNIQUE, "
#     "author varchar(250) NOT NULL, "
#     "rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()
