from db import db


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, unique=True, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f"Movie details:\n" \
               f"- ID: {self.id}\n" \
               f"- Title: {self.title}\n" \
               f"- Year: {self.year}\n" \
               f"- Description: {self.description}\n" \
               f"- Rating: {self.rating}\n" \
               f"- Ranking: {self.ranking}\n" \
               f"- Review: {self.review}\n" \
               f"- Image URL: {self.img_url}\n"
