from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

CHROME_SERVICE = Service("C:/Dev/Driver/chromedriver.exe")
COOKIES_URL = "https://orteil.dashnet.org/cookieclicker/"

with webdriver.Chrome(service=CHROME_SERVICE) as driver:
    driver.get(COOKIES_URL)
    big_cookie = driver.find_element(By.ID, "bigCookie")
    while True:
        try:
            num_cookies = int(driver.find_element(By.ID, "cookies").text.replace(",", "").split(" ")[0])
        except ValueError:
            num_cookies = 0

        products_enabled = driver.find_elements(By.XPATH, "//div[contains(@class, 'product unlocked enabled')]")
        try:
            upgrade_enabled = driver.find_element(By.XPATH, "//div[contains(@class, 'crate upgrade enabled')]")
            upgrade_enabled.click()
        except NoSuchElementException:
            print("No upgrades yet.")

        for product in products_enabled:
            price = int(product.find_element(By.CLASS_NAME, 'price').text.replace(",", ""))
            try:
                owned = int(product.find_element(By.CLASS_NAME, 'owned').text)
            except ValueError:
                owned = 0

            if num_cookies > price:
                product.click()
        big_cookie.click()
