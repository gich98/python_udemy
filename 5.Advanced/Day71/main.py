import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

PAYSCALE_URL = "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors"
CHROME_SERVICE = Service("C:/Dev/Driver/chromedriver.exe")

final_list = []

with webdriver.Chrome(service=CHROME_SERVICE) as driver:
    driver.get(url=PAYSCALE_URL)
    num_pages = int(driver.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/article/div[3]/a[6]").text)
    for _ in range(num_pages):
        if _ != 0:
            driver.get(url=PAYSCALE_URL + f"/page/{_}")
            row_table = driver.find_elements(By.CLASS_NAME, "data-table__row")

            for row in row_table:
                name = row.find_element(By.CLASS_NAME, "csr-col--school-name").text
                row_value = row.find_elements(By.CLASS_NAME, "csr-col--right")
                temp_list = [value.text for value in row_value]
                final_list.append({
                    "name": name,
                    "early": temp_list[0],
                    "mid": temp_list[1],
                })
                # print(f"{name} = MIN -> {temp_list[0]}, MAX -> {temp_list[1]}")

# The rest of the lesson is in the following link:
# https://colab.research.google.com/drive/180tCWsv6uWBbmxPF9cqw4JFFQgJQVijL
