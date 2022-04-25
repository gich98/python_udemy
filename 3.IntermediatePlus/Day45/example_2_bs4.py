from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
score_all = []
articles_list = []
index = 0
articles = soup.find_all(name="a", class_="titlelink")
article_subtexts = soup.find_all(name="td", class_="subtext")
for subtext in article_subtexts:
    if not subtext.find(name="span", class_="score"):
        score_all.append(0)
    else:
        score_all.append(int(subtext.find(name="span", class_="score").getText().split(" ")[0]))

for article in articles:
    temp = {"title": article.getText(), "link": article.get("href"), "score": score_all[index]}
    articles_list.append(temp)
    index += 1

highest_score = 0
index_highest_score = 0
for _ in range(len(articles_list)):
    if articles_list[_].get("score") > highest_score:
        index_highest_score = _
        highest_score = articles_list[_].get("score")

print(articles_list[index_highest_score])
