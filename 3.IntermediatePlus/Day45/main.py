from bs4 import BeautifulSoup

with open(file="100-movies.html") as file:
    content = file.read()
soup = BeautifulSoup(content, "html.parser")
movie_tags = soup.find_all(name="h3", class_="jsx-2692754980")
movie_list = [movie.getText() for movie in movie_tags]
movie_list.reverse()
for _ in movie_list:
    print(_)
