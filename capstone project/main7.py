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
from yfinance import ticker
import datetime

#pip install yfinance python-dateutil seaborn matplotlib

def graphStock():
    stock_symbol = input("Ticker of Stock you have chosen: ")
    start_date = input("Pick start date (DD-MM-YYYY): ")
    end_date = input("Pick end date (DD-MM-YYYY): ")

    # Convert input dates to the correct format (YYYY-MM-DD)
    start_date = datetime.datetime.strptime(start_date, "%d-%m-%Y").strftime("%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date, "%d-%m-%Y").strftime("%Y-%m-%d")

    # Fetch stock data
    stock = yf.Ticker(stock_symbol)
    historical_data = stock.history(start=start_date, end=end_date)

    # Check if data is available
    if historical_data.empty:
        print(f"No data available for {stock_symbol} between {start_date} and {end_date}.")
    else:
        print(historical_data.head())  # Display first few rows of data

        # Plot stock closing price over time
        plt.figure(figsize=(10, 5))
        plt.plot(historical_data.index, historical_data["Close"], label="Closing Price", color="blue")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.title(f"{stock_symbol} Stock Price from {start_date} to {end_date}")
        plt.legend()
        plt.grid()
        plt.show()

    def user_interaction():
        while True:
            continue_choice = input("Would you like me to continue? (yes/no): ").strip().lower()
            if continue_choice == 'yes':
                def get_user_choice():
                    options = {1: "Display a graph for the stock price of a stock for a given period of time.",
                               2: "Print all the statistics for a stock.",
                               3: "Print a specific metric for a stock.",
                               4: "Compare the price of 2 different stocks."}
                    while True:
                        print("Please choose an option:")
                        for key, value in options.items():
                            print(f"{key}. {value}")
                        choice = input("Enter the number corresponding to your choice: ")
                        if choice.isdigit() and int(choice) in options:
                            print(f"You selected option {choice}: {options[int(choice)]}")
                            return int(choice)
                        else:
                            print("Invalid choice. Please enter a number between 1 and 4.")

                user_choice = get_user_choice()
                if user_choice == 1:
                    graphStock()
                elif user_choice == 2:
                    stockStats()
                elif user_choice == 3:
                    stockStatsOneMetricOnly()
                elif user_choice == 4:
                    multipleStock()
            elif continue_choice == 'no':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")
    user_interaction()


def stockStats():
    ticker = input("Enter stock ticker: ").upper().strip()
    stock = yf.Ticker(ticker)

    # Fetch data
    balance_sheet = stock.balance_sheet
    income_statement = stock.financials
    cash_flow = stock.cashflow
    info = stock.info  # Stock market data

    # Print results
    print("Financial Report for", ticker)

    #  Financial Position (Balance Sheet)
    print(" Financial Position (Balance Sheet):")
    for metric in ["Total Assets", "Total Liabilities", "Total Stockholder Equity", "Cash And Cash Equivalents"]:
        if metric in balance_sheet.index:
            print("{}: ${:,.2f}".format(metric, balance_sheet.loc[metric].iloc[0]))

    #  Profitability (Income Statement)
    print(" Profitability (Income Statement):")
    for metric in ["Total Revenue", "Gross Profit", "Operating Income", "Net Income", "EBITDA"]:
        if metric in income_statement.index:
            print("{}: ${:,.2f}".format(metric, income_statement.loc[metric].iloc[0]))

    #  Liquidity & Investment (Cash Flow)
    print(" Liquidity & Investment (Cash Flow):")
    for metric in ["Total Cash From Operating Activities", "Capital Expenditures", "Free Cash Flow"]:
        if metric in cash_flow.index:
            print("{}: ${:,.2f}".format(metric, cash_flow.loc[metric].iloc[0]))

    #  Stock Valuation & Key Ratios
    print(" Stock Valuation & Key Ratios:")
    print("Market Cap: {:,}".format(info.get('marketCap', 'N/A')))
    print("P/E Ratio: {}".format(info.get('trailingPE', 'N/A')))
    print("Dividend Yield: {}%".format(info.get('dividendYield', 'N/A')))
    print("52-Week High: {}".format(info.get('fiftyTwoWeekHigh', 'N/A')))
    print("52-Week Low: {}".format(info.get('fiftyTwoWeekLow', 'N/A')))

    def user_interaction():
        while True:
            continue_choice = input("Would you like me to continue? (yes/no): ").strip().lower()
            if continue_choice == 'yes':
                def get_user_choice():
                    options = {1: "Display a graph for the stock price of a stock for a given period of time.",
                               2: "Print all the statistics for a stock.",
                               3: "Print a specific metric for a stock.",
                               4: "Compare the price of 2 different stocks."}
                    while True:
                        print("Please choose an option:")
                        for key, value in options.items():
                            print(f"{key}. {value}")
                        choice = input("Enter the number corresponding to your choice: ")
                        if choice.isdigit() and int(choice) in options:
                            print(f"You selected option {choice}: {options[int(choice)]}")
                            return int(choice)
                        else:
                            print("Invalid choice. Please enter a number between 1 and 4.")

                user_choice = get_user_choice()
                if user_choice == 1:
                    graphStock()
                elif user_choice == 2:
                    stockStats()
                elif user_choice == 3:
                    stockStatsOneMetricOnly()
                elif user_choice == 4:
                    multipleStock()
            elif continue_choice == 'no':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")
    user_interaction()

def stockStatsOneMetricOnly():
    ticker = input("Enter stock ticker: ").upper().strip()
    metric = input("Enter the metric you want: ").strip()

    # Fetch the stock data
    stock = yf.Ticker(ticker)

    # Try to fetch the specified metric
    metric_value = stock.info.get(metric, 'Data not available')

    # Print the result
    print("{} for {}: {}".format(metric, ticker, metric_value))

    def user_interaction():
        while True:
            continue_choice = input("Would you like me to continue? (yes/no): ").strip().lower()
            if continue_choice == 'yes':
                def get_user_choice():
                    options = {1: "Display a graph for the stock price of a stock for a given period of time.",
                               2: "Print all the statistics for a stock.",
                               3: "Print a specific metric for a stock.",
                               4: "Compare the price of 2 different stocks."}
                    while True:
                        print("Please choose an option:")
                        for key, value in options.items():
                            print(f"{key}. {value}")
                        choice = input("Enter the number corresponding to your choice: ")
                        if choice.isdigit() and int(choice) in options:
                            print(f"You selected option {choice}: {options[int(choice)]}")
                            return int(choice)
                        else:
                            print("Invalid choice. Please enter a number between 1 and 4.")

                user_choice = get_user_choice()
                if user_choice == 1:
                    graphStock()
                elif user_choice == 2:
                    stockStats()
                elif user_choice == 3:
                    stockStatsOneMetricOnly()
                elif user_choice == 4:
                    multipleStock()
            elif continue_choice == 'no':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")
    user_interaction()


def multipleStock():
    stocks = input("Which stocks (tickers) do you want: ").split()
    start_date = input('Pick a start date (YYYY-MM-DD): ')
    end_date = input('Pick an end date (YYYY-MM-DD): ')
    for stock in stocks:
        color = random.choice(["r", "b", "g", "y", "p", "o", "c", "m", "k"])
        data = yf.Ticker(stock).history(start=start_date, end=end_date)
        sns.set_style('whitegrid'); plt.style.use("fivethirtyeight")
        plt.plot(data['Open'], color=color, label=stock)
    plt.legend(); plt.show()

    def user_interaction():
        while True:
            continue_choice = input("Would you like me to continue? (yes/no): ").strip().lower()
            if continue_choice == 'yes':
                def get_user_choice():
                    options = {1: "Display a graph for the stock price of a stock for a given period of time.",
                               2: "Print all the statistics for a stock.",
                               3: "Print a specific metric for a stock.",
                               4: "Compare the price of 2 different stocks."}
                    while True:
                        print("Please choose an option:")
                        for key, value in options.items():
                            print(f"{key}. {value}")
                        choice = input("Enter the number corresponding to your choice: ")
                        if choice.isdigit() and int(choice) in options:
                            print(f"You selected option {choice}: {options[int(choice)]}")
                            return int(choice)
                        else:
                            print("Invalid choice. Please enter a number between 1 and 4.")

                user_choice = get_user_choice()
                if user_choice == 1:
                    graphStock()
                elif user_choice == 2:
                    stockStats()
                elif user_choice == 3:
                    stockStatsOneMetricOnly()
                elif user_choice == 4:
                    multipleStock()
            elif continue_choice == 'no':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")
    user_interaction()



#-------------------------------------------------------------------------------------------------------------------

def get_user_choice():
    options = {1: "Display a graph for the stock price of a stock for a given period of time.",
               2: "Print all the statistics for a stock.",
               3: "Print a specific metric for a stock.",
               4: "Compare the price of 2 different stocks.",
               5: "None"}
    while True:
        print("Please choose an option:")
        for key, value in options.items():
            print(f"{key}. {value}")
        choice = input("Enter the number corresponding to your choice: ")
        if choice.isdigit() and int(choice) in options:
            print(f"You selected option {choice}: {options[int(choice)]}")  # Print the corresponding description
            return int(choice)
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

user_choice = get_user_choice()

if user_choice == 1:
    graphStock()
elif user_choice == 2:
    stockStats()
elif user_choice == 3:
    stockStatsOneMetricOnly()
elif user_choice == 4:
    multipleStock()
elif user_choice == 5:
    exit(5)

