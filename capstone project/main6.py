import random
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
#from yahoofinance import Ticker

'''
def returnInvest():
    
    stock = input("Which stocks do you want(Write ticker of company)")
    bought_date = input('Pick a start date.')
    sale_date = input('Pick an end date.')
    stock_data = yf.Ticker(stock)
    stock_data_history = stock_data.history(start=bought_date, end=sale_date)
    #print(stock_data_history)
    print(stock_data_history['Open'][bought_date])

    stock_symbol = "AAPL"
    date = "2023-10-10"
    # Fetch the historical data
    stock = yf.Ticker(stock_symbol)
    historical_data = stock.history(start=date, end=date)
    closing_price = historical_data['Close'].iloc[0]
    print(closing_price)
    


returnInvest()
'''
'''

def getStockOnGivenDate(stock_symbol, string_date):
    start_date = datetime.datetime.strptime('string_date', "%d%m%Y").date()
    end_date = start_date + datetime.timedelta(days=1)

    stock = yf.Ticker(stock_symbol)
    historical_data = stock.history(start=start_date, end=end_date)
    print(historical_data)

    closing_price = historical_data['Close'].iloc[0]
    return closing_price

'''
import datetime
import yfinance as yf


#
'''
def getStockOnGivenDate(stock_symbol, string_date):
    start_date = datetime.datetime.strptime(string_date, "%d%m%Y").date()
    end_date = start_date + datetime.timedelta(days=1)

    stock = yf.Ticker(stock_symbol)
    historical_data = stock.history(start=start_date, end=end_date)





