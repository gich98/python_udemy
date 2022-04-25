from bs4 import BeautifulSoup

with open(file="website.html", encoding="utf-8") as website:
    content = website.read()

soup = BeautifulSoup(content, "html.parser")
all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)
for a in all_anchor_tags:
    print(a.get("href"))

h3_list = soup.find_all(name="h3", class_="heading")
print(h3_list)

company_url = soup.select_one(selector="p a")
print(company_url)

h1 = soup.select_one(selector="#name")
print(h1)

class_heading = soup.select(selector=".heading")
print(class_heading)
