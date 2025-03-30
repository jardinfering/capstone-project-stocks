import random

#import random
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from yahoofinance import HistoricalPrices
from datetime import datetime, timedelta
from dateutil.relativedelta import *
from yfinance import Ticker
from yfinance import ticker

'''
def multipleStock():
#   nofstock = int(input("How many stocks do you want to plot the data for upto 5"))
#  for nofstock in range (5):
    stocks = input("Which stocks do you want(Write ticker of company)")
    stocks = stocks.split()
    #stock = stock.split(",")
    print(stocks)
    start_date = input('Pick a start date.')
    end_date = input('Pick an end date.')
    for i in range (len(stocks)):
        stock_data = stocks.ticker(start=start_date, end=end_date)
    stock = yf.Ticker(ticker)
    sns.set_style('whitegrid')
    plt.style.use("fivethirtyeight")
    plt.plot(stock_data['Open'], color = 'r')
    plt.show()


multipleStock()

aapl,googl,msft -> split(",") - ["aapl", "goog", "msft"]

for stock on stocks:
    build_plot(stock)

'''


def multipleStock():
    stocks = input("Which stocks do you want(Write ticker of company)")
    stocks = stocks.split()
    print(stocks)
    start_date = input('Pick a start date.')
    end_date = input('Pick an end date.')
    for stock in stocks:
        random_colors  = ["r", "b", "g", "y", "p", "o", "c", "m", "k"]
        random_color = random.choice(random_colors)
        stock_data = yf.Ticker(stock)
        stock_data_history = stock_data.history(start=start_date, end=end_date)
        sns.set_style('whitegrid')
        plt.style.use("fivethirtyeight")
        plt.plot(stock_data_history['Open'], color = random_color)
    plt.show()

multipleStock()












