from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

PROMISED_DOWN = 50
PROMISED_UP = 20
CHROME_SERVICE = Service("C:/Dev/Driver/chromedriver.exe")
TWITTER_USERNAME = "username"
TWITTER_PASSWORD = "password"
SPEED_TEST_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/login/"


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(url=SPEED_TEST_URL)
        wait_driver = WebDriverWait(driver=self.driver, timeout=120)
        consent_cookies = wait_driver.until(
            expected_conditions.presence_of_element_located((By.ID, "_evidon-banner-acceptbutton")))
        consent_cookies.click()
        speed_test_a = wait_driver.until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]")
            )
        )
        speed_test_a.click()
        while self.driver.current_url == SPEED_TEST_URL:
            self.down = wait_driver.until(
                expected_conditions.presence_of_element_located(
                    (By.CLASS_NAME, "download-speed")
                )
            ).text
            self.up = wait_driver.until(
                expected_conditions.presence_of_element_located(
                    (By.CLASS_NAME, "upload-speed")
                )
            ).text
        print(f"Download: {self.down}, Upload: {self.up}")

    def tweet_at_provider(self):
        self.driver.get(url=TWITTER_URL)
        wait_driver = WebDriverWait(driver=self.driver, timeout=5)
        username = wait_driver.until(
            expected_conditions.presence_of_element_located(
                (By.NAME, "text")
            )
        )
        username.send_keys(TWITTER_USERNAME)
        username.send_keys(Keys.ENTER)
        password = wait_driver.until(
            expected_conditions.presence_of_element_located(
                (By.NAME, "password")
            )
        )
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        new_tweet = wait_driver.until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, "//*[@id='react-root']/div/div/div[2]/header/div/div/div/div[1]/div[3]/a")
            )
        )
        new_tweet.click()
        tweet = wait_driver.until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div"
                           "/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label"
                           "/div[1]/div/div/div/div/div[2]/div/div/div/div")
            )
        )
        if float(self.down) < PROMISED_DOWN or float(self.up) < PROMISED_UP:
            tweet.send_keys(f"Hey @username2, why is my internet speed {self.down}down/{self.up}up"
                            f" when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")
        else:
            tweet.send_keys(f"Hey @vkind88976000, You did what you promised to my internet speed is "
                            f"{self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}.")
        confirm_tweet = wait_driver.until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div"
                           "/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]")
            )
        )
        confirm_tweet.click()

