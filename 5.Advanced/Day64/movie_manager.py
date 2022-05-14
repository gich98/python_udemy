import requests
from movie import Movie


class MovieManager:
    
    def __init__(self, db, movie_db):
        self.db = db
        self.movie_db = movie_db

    def get_all_movies(self):
        return self.db.session.query(self.movie_db).all()

    def get_movie_by_id(self, movie_id):
        return self.movie_db.query.get(movie_id)

    def update_movie_rating(self, movie, rating, review):
        movie.rating = rating
        movie.review = review
        self.update_movies_ranking()
        self.db.session.commit()

    def update_movies_ranking(self):
        movies = self.get_all_movies()
        movies_sorted = sorted(movies, key=lambda a: a.rating, reverse=True)
        for rank, movie in enumerate(movies_sorted):
            movie.ranking = rank + 1
        self.db.session.commit()

    def delete_movie(self, movie_id):
        movie = self.get_movie_by_id(movie_id)
        self.db.session.delete(movie)
        self.db.session.commit()

    def add_movie(self, movie_id):
        movie = self.tmdb_movie_details(movie_id)
        self.db.session.add(movie)
        self.update_movies_ranking()
        self.db.session.commit()

    @staticmethod
    def tmdb_search_movie(movie_name):
        tmdb_search_endpoint = "https://api.themoviedb.org/3/search/movie"
        params = {
            "api_key": "af7c764de3d25c93c54165b6e80db5d1",
            "query": movie_name,
            "language": "en-US",
            "adult": False,
        }
        response = requests.get(url=tmdb_search_endpoint, params=params)
        return response.json().get("results")

    @staticmethod
    def tmdb_movie_details(movie_id):
        tmdb_movie_endpoint = "https://api.themoviedb.org/3/movie/" + movie_id
        params = {
            "api_key": "af7c764de3d25c93c54165b6e80db5d1",
            "language": "en-US",
        }
        response = requests.get(url=tmdb_movie_endpoint, params=params).json()
        image_url = "https://image.tmdb.org/t/p/w500/" + response.get("poster_path")
        new_movie = Movie(
            id=response.get("id"),
            title=response.get("original_title"),
            year=response.get("release_date").split("-")[0],
            description=response.get("overview"),
            rating=0,
            ranking=1,
            review="No review yet.",
            img_url=image_url
        )
        return new_movie
