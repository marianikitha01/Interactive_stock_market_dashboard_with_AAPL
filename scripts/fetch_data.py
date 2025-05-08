import os
import pandas as pd
import requests

API_KEY = '***'

# Create a 'data' directory if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

def fetch_raw_data(symbol):
    """Fetch daily stock data and save it as CSV."""
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}&datatype=csv'
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(f'data/{symbol}_raw.csv', 'wb') as f:
                f.write(response.content)
            print(f"Data for {symbol} saved as {symbol}_raw.csv")
        else:
            print(f"Error fetching data for {symbol}: {response.status_code}")
    except Exception as e:
        print(f"Error fetching data: {e}")

# Fetch data for AAPL
fetch_raw_data('AAPL')
