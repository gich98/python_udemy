from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

CHROME_SERVICE = Service("C:/Dev/Driver/chromedriver.exe")
URL = "http://secure-retreat-92358.herokuapp.com"

# with webdriver.Chrome(service=CHROME_SERVICE) as driver:
driver = webdriver.Chrome(service=CHROME_SERVICE)
driver.get(URL)
# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()
# random_article = driver.find_element(By.LINK_TEXT, "Current events")
# random_article.click()
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("FirstName")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("LastName")
email = driver.find_element(By.NAME, "email")
email.send_keys("firstlast@email.com")
email.send_keys(Keys.ENTER)
