import argparse
import pandas as pd
import yfinance as yf

# Define the start and end dates
start_date = '2013-01-01'
end_date = '2023-03-01'

# Create the argument parser
parser = argparse.ArgumentParser(description='Download stock data using Yahoo Finance API')
parser.add_argument('ticker', type=str, help='Stock ticker symbol')

# Parse the command-line arguments
args = parser.parse_args()

# Retrieve the ticker symbol from the parsed arguments
ticker = args.ticker

# Download the stock data using yfinance and write to CSV
data = yf.download(ticker, start=start_date, end=end_date)
data.to_csv(f'data/{ticker}.csv')
