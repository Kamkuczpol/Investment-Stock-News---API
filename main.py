import json
import pprint

import requests
import datetime


# STEP 1: When stock price increase/decreases by 5% between yesterday and
# the day before yesterday then print("Get News").

# TODO 1. - Get yesterday's closing stock price.

r = requests.get('https://www.alphavantage.co/query?'
                 'function=TIME_SERIES_DAILY&symbol=TSLA'
                 '&apikey=U3C3PJT28GJQJP6A')

data = r.json()

closing_price_yesterday = data['Time Series (Daily)']['2022-06-17']['4. close']
print("Closing stock price: ", closing_price_yesterday)
float_closing_price_yesterday = float(closing_price_yesterday)


# TODO 2. - Get the day before yesterday's closing stock price
closing_price_the_day_before_yesterday = data['Time Series (Daily)']['2022-06-16']['4. close']
print("Closing price the day before yesterday: ", closing_price_the_day_before_yesterday)
float_closing_price_the_day_before_yesterday = float(closing_price_the_day_before_yesterday)


# TODO 3. - Find the positive difference between 1 and 2.
# difference = closing_price_yesterday - closing_price_the_day_before_yesterday
# pos_difference = abs(int(difference))


# TODO 4. - Work out the percentage difference in price between closing
#  price yesterday and closing price the day before yesterday.
percentage_difference = float_closing_price_yesterday / float_closing_price_the_day_before_yesterday
print("percentage_difference: ", round(percentage_difference, 2))


# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percentage_difference > 5:
    print("Get news")


# STEP 2: Instead of printing ("Get News"), actually get the first 3 news
# pieces for the COMPANY_NAME.


# TODO 6. - Instead of printing ("Get News"), use the News API to get
#  articles related to the COMPANY_NAME.
today_date = datetime.datetime.today()


params = {
    "q": "tesla",
    "from": today_date.day,
    "sortBy": "publishedAt",
    "apiKey": "1051f15475d343a7aa34fc90f60a1e63"
}

re = requests.get("https://newsapi.org/v2/everything?", params)

news = re.json()
# pprint.pprint(news)


# TODO 7. - Use Python slice operator to create a list that contains
#  the first 3 articles.
#  Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


for article in news["articles"][:3]:
    # pprint.pp(article)
    print("Title: ", article["title"])
    print("Description ", article["description"])
    print("Url ", article["url"])
    print()

# STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description
# to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and
#  description using list comprehension.

# TODO 9. - Send each article as a separate message via Twilio.


# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
