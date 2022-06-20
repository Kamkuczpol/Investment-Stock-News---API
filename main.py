from twilio.rest import Client
import requests
from datetime import datetime

# TODO 1. - Get yesterday's closing stock price.
symbol = "TSLA"
company_name = "Tesla"

r = requests.get('https://www.alphavantage.co/query?'
                 'function=TIME_SERIES_DAILY&symbol=' + symbol +
                 '&apikey=demo')

data = r.json()["Time Series (Daily)"]

data_list = [value for day, value in data.items()]

yesterday_price = data_list[0]['4. close']

# TODO 2. Get the day before yesterday's closing stock price
day_before_yesterday_price = data_list[1]['4. close']

# TODO 3. - Work out the percentage difference in price between closing
#  price yesterday and closing price the day before yesterday.
diff_percentage = round(((float(yesterday_price) / float(day_before_yesterday_price)) - 1) * 100, 2)

up_down = None

if diff_percentage > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# TODO 4. - If TODO4 percentage is greater than 5 then print("Get News").
today_date = datetime.today()

if float(diff_percentage) > 1:
    params = {
        "q": company_name,
        "from": today_date.day,
        "sortBy": "publishedAt",
        "apiKey": "PUT_YOUR_NEWS_API"
    }

    re = requests.get("https://newsapi.org/v2/everything?", params)

    news = re.json()["articles"]

    for article in news[:3]:
        print("Title: ", article["title"])
        print("Description ", article["description"])
        print("Url ", article["url"])
        print()

    # TODO 5. - Use the News API to get articles related to the COMPANY_NAME.

    # TODO 6. - Create a list that contains the first 3 articles.

    formatted_articles = [
        f"{symbol}: {up_down}{diff_percentage}%\nHeadline: {article['title']} \nlink:{article['url']} " for article in
        news[:3]]

    # TODO 7. - Send each article as a separate message via Twilio.

    account_sid = 'PUT_YOUR_SID_NUMBER'
    auth_token = 'PUT_YOUR_TOKEN_FROM_TWILIO'

    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages \
            .create(
            body=article,
            from_='+PUT_YOUR_NUMBER_FROM_TWILIO',
            to='+PUT_YOUR_NUMBER'
        )
