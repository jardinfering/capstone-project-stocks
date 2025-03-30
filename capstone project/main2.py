import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from yahoofinance import HistoricalPrices

#req = HistoricalPrices('AAPL','2015-01-01','2017-12-12')
'''
ticker = input("ticker of stock")
start_date = '2010-01-01'
end_date = '2020-12-31'

# Fetch historical data
stock = yf.Ticker(ticker)
historical_data = stock.history(start=start_date, end=end_date)

# Display the historical data
print(historical_data)
plt.plot(historical_data)
plt.show()
'''
'''
balance_sheet.loc['Cash Financial'].plot(kind='bar')
plt.title('Cash Financial')
plt.show()

balance_sheet.loc['Share Issued'].plot(kind='bar')
plt.title('Share Issued')
plt.show()

balance_sheet.loc['Total Debt'].plot(kind='bar')
plt.title('Total Debt')
plt.show()

balance_sheet.loc['Cash Equivalents'].plot(kind='bar')
plt.title('Cash Equivalents')
plt.show()
'''
'''

# Plotting styles
sns.set_style('whitegrid')
plt.style.use("fivethirtyeight")

# Define tech stocks
tech_list = ['AAPL', 'GOOG', 'MSFT', 'AMZN']

# Set up end and start dates
end = datetime.now()
start = datetime(end.year - 1, end.month, end.day)

# Create a dictionary to store data
stock_data = {}

# Download data for each stock and store it in the dictionary
for stock in tech_list:
    stock_data[stock] = yf.download(stock, start=start, end=end)

# Combine all data into a single DataFrame for analysis
combined_data = pd.concat(stock_data, axis=1)

# Add company names to the data (example usage)
company_name_map = dict(zip(tech_list, ["Apple", "Google", "Microsoft", "Amazon"]))
'''
'''
# Example: Accessing and printing data for Apple
print("Apple's Stock Data:")


print(stock_data['AAPL'])
print(stock_data['GOOG'])
print(stock_data['MSFT'])
print(stock_data['AMZN'])

# Display the combined data structure
print("\nCombined Data Columns:")
print(combined_data.columns)
'''
'''
# Example Plot: Apple Stock Price
plt.figure(figsize=(10, 6))
stock_data['AAPL']['Close'].plot(title="Apple Stock Price (Last Year)")
plt.xlabel("Date")
plt.ylabel("Close Price (USD)")
plt.show()

plt.figure(figsize=(10, 6))
stock_data['GOOG']['Close'].plot(title="Google Stock Price (Last Year)")
plt.xlabel("Date")
plt.ylabel("Close Price (USD)")
plt.show()

plt.figure(figsize=(10, 6))
stock_data['MSFT']['Close'].plot(title="Microsoft Stock Price (Last Year)")
plt.xlabel("Date")
plt.ylabel("Close Price (USD)")
plt.show()

plt.figure(figsize=(10, 6))
stock_data['AMZN']['Close'].plot(title="Amazon Stock Price (Last Year)")
plt.xlabel("Date")
plt.ylabel("Close Price (USD)")
plt.show()
'''
'''
company_list = ['AAPL', 'GOOG', 'MSFT', 'AMZN']

for i, company in enumerate(company_list, 1):
    plt.subplot(2, 2, i)
#    company['Adj Close'].plot()
    plt.ylabel('Adj Close')
    plt.xlabel(None)
    plt.title(f"Closing Price of {tech_list[i - 1]}")

plt.show()
'''
'''
company_list = ['AAPL', 'GOOG', 'MSFT', 'AMZN']

'''

# Get user input
ticker = input("Enter stock ticker: ").upper().strip()
stock = yf.Ticker(ticker)

# Fetch data
data = {
    "Financial Position (Balance Sheet)": stock.balance_sheet,
    "Profitability (Income Statement)": stock.financials,
    "Liquidity & Investment (Cash Flow)": stock.cashflow,
}
info = stock.info  # Stock market data

# Metrics to extract
metrics = {
    "Financial Position (Balance Sheet)": ["Total Assets", "Total Liabilities", "Total Stockholder Equity",
                                           "Cash And Cash Equivalents", "Long Term Debt"],
    "Profitability (Income Statement)": ["Total Revenue", "Gross Profit", "Operating Income", "Net Income", "EBITDA"],
    "Liquidity & Investment (Cash Flow)": ["Total Cash From Operating Activities", "Capital Expenditures",
                                           "Free Cash Flow"],
    "Stock Valuation & Key Ratios": {"Market Cap": "marketCap", "P/E Ratio": "trailingPE",
                                     "Dividend Yield": "dividendYield", "52-Week High": "fiftyTwoWeekHigh",
                                     "52-Week Low": "fiftyTwoWeekLow"},
}

# Function to fetch data safely
def get_metric(data, key):
    try:
        return f"${data.loc[key][0]:,.2f}"
    except (KeyError, IndexError, TypeError):
        return "N/A"

def get_info(key):
    return f"{info.get(key, 'N/A'):,}" if isinstance(info.get(key), (int, float)) else "N/A"

# Print results
print(f"\n📊 Financial Report for {ticker}\n")
for section, keys in metrics.items():
    print(f"📌 {section}:")
    if isinstance(keys, list):  # Balance sheet, income statement, cash flow
        for key in keys:
            print(f"{key}: {get_metric(data[section], key)}")
    else:  # Stock valuation (from stock.info)
        for key, info_key in keys.items():
            print(f"{key}: {get_info(info_key)}")
    print()


