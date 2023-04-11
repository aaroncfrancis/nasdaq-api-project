import time 
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

api_key = '0K0L52MI81VV967R'

ts = TimeSeries(key=api_key, output_format='pandas')

"""Retrieve real-time stock data ex: AAPL"""
data = ts.get_quote_endpoint(symbol='TLT')
print(data[0])

print(type(data[0]))