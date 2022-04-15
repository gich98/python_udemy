import requests
import html
import datetime as dt
import smtplib

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
AV_STOCK_ENDPOINT = "https://www.alphavantage.co/query"
AV_STOCK_TIME_SERIES = "TIME_SERIES_DAILY"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
AV_API_KEY = "TZ1RI4NSKZQNMW5G"
NEWS_API_KEY = "bee209d9fd0a4e21a92decb585b99860"
current_date = dt.datetime.now().strftime("%Y-%m-%d-1")
MY_EMAIL = "vg.checkrain@gmail.com"
MY_PASSWORD = "1234567890asD."
# STEP 1: Use https://www.alphavantage.co
# When CLOSE STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo
av_stock_params = {
    "function": AV_STOCK_TIME_SERIES,
    "symbol": STOCK,
    "apikey": AV_API_KEY,
}
# q=Tesla&nbsp;Inc&from=2022-03-13&sortBy=publishedAt&apiKey=bee209d9fd0a4e21a92decb585b99860
news_params = {
    "qInTitle": html.escape(COMPANY_NAME),
    "from": current_date,
    "sortBy": "popularity",
    "apiKey": NEWS_API_KEY,
}


def check_stock():
    response_stock = requests.get(url=AV_STOCK_ENDPOINT, params=av_stock_params)
    response_stock.raise_for_status()
    daily_stocks = response_stock.json()["Time Series (Daily)"]
    yesterday_stock = float(list(daily_stocks.values())[0]["4. close"])
    before_yesterday_stock = float(list(daily_stocks.values())[1]["4. close"])
    delta = round(((yesterday_stock - before_yesterday_stock) * 100) / yesterday_stock, 2)
    if abs(delta) >= 3:
        print(f"Get News delta is {delta}")
    else:
        print(f"Nothing important, the delta is only {delta}")
    return delta


# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def get_top_news():
    response_news = requests.get(url=NEWS_ENDPOINT, params=news_params)
    response_news.raise_for_status()
    top_3_news = response_news.json()["articles"][:3]
    return top_3_news


# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.
def send_email(delta, top_3_news):
    # print("Sending...")
    with smtplib.SMTP(host="smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        for new in top_3_news:
            title = new.get("title").encode('ascii', 'ignore')
            content = new.get("content").encode('ascii', 'ignore')
            print(delta)
            print(title)
            print(content)
            print(new.get("content"))
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="gchen.svago@gmail.com",
                msg=f"Subject:TSLA {delta}\n\n"
                    f"{title}"
                    f"{content}"
            )


delta_tesla = check_stock()
if abs(delta_tesla) >= 3:
    top_news = get_top_news()
    send_email(delta=delta_tesla, top_3_news=top_news)


