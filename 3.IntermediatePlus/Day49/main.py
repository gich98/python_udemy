import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def signin(wait_driver_):
    username = wait_driver.until(expected_conditions.presence_of_element_located((By.ID, "username")))
    password = wait_driver.until(expected_conditions.presence_of_element_located((By.ID, "password")))
    signin_button_ = wait_driver.until(expected_conditions.presence_of_element_located(
        (By.XPATH, "//*[@id='organic-div']/form/div[3]/button")
    ))
    username.send_keys("email@email.com")
    password.send_keys("password")
    signin_button_.click()


CHROME_SERVICE = Service("C:/Dev/Driver/chromedriver.exe")
LINKEDIN_URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location" \
               "=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"

with webdriver.Chrome(service=CHROME_SERVICE) as driver:
    driver.get(url=LINKEDIN_URL)
    signin_button = driver.find_element(By.XPATH, "/html/body/div[3]/header/nav/div/a[2]")
    signin_button.click()

    wait_driver = WebDriverWait(driver=driver, timeout=10)
    signin(wait_driver)
    easy_apply_button = wait_driver.until(expected_conditions.presence_of_element_located(
        (By.CLASS_NAME, "jobs-apply-button")
    ))
    easy_apply_button.click()

    close_button = wait_driver.until(expected_conditions.presence_of_element_located(
        (By.CLASS_NAME, "artdeco-modal__dismiss")
    ))
    close_button.click()

    discard_button = wait_driver.until(expected_conditions.presence_of_element_located(
        (By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")
    ))
    discard_button.click()