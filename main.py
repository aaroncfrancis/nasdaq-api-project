"""This version will use standard API loading method"""
import requests

symbol = input('What stock would you like to get data for?\n')

url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey=0K0L52MI81VV967R"
r = requests.get(url)
data = r.json()

print(data)

