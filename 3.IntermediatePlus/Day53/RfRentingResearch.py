import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

RF_RENTING_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLScv5oPer00UppsklFwC472d4yUKk8Qja1fjqft18g1xNnHyig/viewform?usp=sf_link"
CHROME_SERVICE = Service("C:/Dev/Driver/chromedriver.exe")
ADDRESS_XPATH = "//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input"
PRICE_XPATH = "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input"
LINK_XPATH = "//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input"
SEND_XPATH = "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div"
SEND_AGAIN_XPATH = "/html/body/div[1]/div[2]/div[1]/div/div[4]/a"


class RfRentingResearch:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")
        self.driver = webdriver.Chrome(service=CHROME_SERVICE, chrome_options=options)
        self.driver.get(url=RF_RENTING_FORM_URL)

    def insert_property(self, address, price, link):
        address_input = self.driver.find_element(By.XPATH, ADDRESS_XPATH)
        time.sleep(1)
        address_input.send_keys(address)
        price_input = self.driver.find_element(By.XPATH, PRICE_XPATH)
        price_input.send_keys(price)
        link_input = self.driver.find_element(By.XPATH, LINK_XPATH)
        link_input.send_keys(link)
        send_button = self.driver.find_element(By.XPATH, SEND_XPATH)
        send_button.click()
        send_again_button = self.driver.find_element(By.XPATH, SEND_AGAIN_XPATH)
        send_again_button.click()
