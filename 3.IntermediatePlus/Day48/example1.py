from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_SERVICE = Service("C:/Dev/Driver/chromedriver.exe")

with webdriver.Chrome(service=CHROME_SERVICE) as driver:
    driver.get("https://www.python.org")

    # search_bar = driver.find_element(By.ID, "id-search-field")
    # print(search_bar.get_attribute("placeholder"))
    #
    # logo = driver.find_element(By.CLASS_NAME, "python-logo")
    # print(logo.size)
    #
    # documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
    # print(documentation_link.text)
    #
    # bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
    # print(bug_link.get_property("href"))
    #
    # download_subtitle = driver.find_element(By.XPATH, '//*[@id="container"]/li[2]/a')
    # print(download_subtitle.text)

    events = driver.find_elements(By.CSS_SELECTOR, ".event-widget li")
    events_dict = {
        key: {
            "time": event.text.split("\n")[0],
            "name": event.text.split("\n")[1],
        } for key, event in enumerate(events)}
    print(events_dict)
