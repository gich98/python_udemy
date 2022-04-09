import smtplib
import pandas
import datetime as dt
import random
import os

NAME_PLACEHOLDER = "[NAME]"
MY_EMAIL = "example@gmail.com"
MY_PASSWORD = "password."

data = pandas.read_csv("birthdays.csv")
birthdays = data.to_dict(orient="records")
letters = os.listdir("./letter_templates")
random_letter = random.choice(letters)
current_day = dt.datetime.now().day
current_month = dt.datetime.now().month

for birthday in birthdays:
    if (birthday["month"] == current_month) and (birthday["day"] == current_day):
        # Create letter
        with open(file=f"./letter_templates/{random_letter}") as letter_file:
            content_letter = letter_file.readlines()
            content_letter = "".join(content_letter)
            content_letter = content_letter.replace(NAME_PLACEHOLDER, birthday["name"])
        # Send mail
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday["email"],
                msg=f"Subject:Happy Birthday!\n\n{content_letter}"
            )
    else:
        print(f"It's not your birthday, {birthday['name']}")
