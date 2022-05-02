from bs4 import BeautifulSoup
import requests
from datetime import datetime

ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/2_p/?searchQueryState=%7B%22mapBounds%22%3A%7B%22west%22%3A-122.97303236914063%2C%22east%22%3A-121.89362563085938%2C%22south%22%3A37.46800922594818%2C%22north%22%3A38.08130180319625%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22pagination%22%3A%7B%22currentPage%22%3A{SELF_PAGE}%7D%7D"

ZILLOW_SHORT_URL = "https://www.zillow.com"
# XPATH_NEXT_BUTTON = "//*[@id="grid-search-result-s"]/div[3]/nav/ul/li[10]/a"
XPATH_UL = "//*[@id='grid-search-results']/ul"
BROWSER_HEADER = {
    "Accept-Language": "en-US",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"
}


class ZillowRenting:

    def __init__(self):
        self.page = 1
        self.properties_dict = self.get_properties()

    def get_properties(self):
        response = requests.get(url=ZILLOW_URL.replace("{SELF_PAGE}", str(self.page)), headers=BROWSER_HEADER)
        soup = BeautifulSoup(response.text, "html.parser")
        list_properties_price = soup.find_all(name="div", class_="list-card-price")
        list_properties_address = soup.find_all(name="address", class_="list-card-addr")
        list_properties_link = soup.find_all(name="a", class_="list-card-link")
        self.page += 1
        return {
            address.getText(): {
                "address": address.getText(),
                "link": ZILLOW_SHORT_URL+link["href"] if link["href"].find(ZILLOW_SHORT_URL) else link["href"],
                "price": price.getText(),
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
            for address, link, price
            in zip(list_properties_address, list_properties_link, list_properties_price)
        }
