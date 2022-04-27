import requests
from bs4 import BeautifulSoup
import smtplib

PRODUCT_AMAZON_URL = "https://www.amazon.it/LG-24GN53A-UltraGear-1920x1080-FreeSync/dp/B088BN751K"
BUY_PRICE = 150
MY_EMAIL = "from@gmail.com"
MY_PASSWORD = "password."
YOUR_EMAIL = "to@gmail.com"

headers = {
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.72"
}

r_amazon = requests.get(url=PRODUCT_AMAZON_URL, headers=headers)
r_amazon.raise_for_status()
soup = BeautifulSoup(r_amazon.content, "html.parser")
tag_price = soup.find(name="span", class_="a-offscreen")
tag_name = soup.select_one(selector="#productTitle")
if tag_price is not None:
    product_price = float(tag_price.getText().replace("€", "").replace(",", "."))
    product_name = tag_name.getText().lstrip()
    if product_price <= BUY_PRICE:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=YOUR_EMAIL,
                msg=f"Subject:{product_name}!\n\nThe price of {product_name} is only {product_price}"
            )
    else:
        print(f"The price is too high. Right now is {product_price}, let's wait until it'll be cheaper.")
else:
    print("Error request")
