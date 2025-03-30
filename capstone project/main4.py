import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from yahoofinance import HistoricalPrices
from datetime import datetime, timedelta
from dateutil.relativedelta import *


#def custom_date():
start_date = input('Pick a start date.')
end_date = input('Pick an end date.')

ticker1 = input('Pick a company to plot out the data for.')
# Fetch historical data
stock = yf.Ticker(ticker1)
historical_data = stock.history(start=start_date, end=end_date)
# Display the historical data

#custom_date()

ticker2 = input('Pick a different company to plot out the data for.')
# Fetch historical data
stock = yf.Ticker(ticker2)
historical_data2 = stock.history(start=start_date, end=end_date)
# Display the historical data
print(historical_data)
print(historical_data2)
#custom_date()

sns.set_style('whitegrid')
plt.style.use("fivethirtyeight")
#plt.plot(historical_data['Open'], historical_data2['Open'])
plt.plot(historical_data['Open'], color = 'r')
plt.plot(historical_data2['Open'], color = 'y')
plt.show()
