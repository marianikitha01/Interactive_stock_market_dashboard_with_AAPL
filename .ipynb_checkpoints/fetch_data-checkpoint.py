{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7dff4caf-070b-4324-a562-256323bd2f86",
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'data/AAPL_raw.csv'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 11\u001b[0m\n\u001b[0;32m      8\u001b[0m url \u001b[38;5;241m=\u001b[39m \u001b[38;5;124mf\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mhttps://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=\u001b[39m\u001b[38;5;132;01m{\u001b[39;00msymbol\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m&outputsize=full&apikey=\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mAPI_KEY\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m&datatype=csv\u001b[39m\u001b[38;5;124m'\u001b[39m\n\u001b[0;32m     10\u001b[0m response \u001b[38;5;241m=\u001b[39m requests\u001b[38;5;241m.\u001b[39mget(url)\n\u001b[1;32m---> 11\u001b[0m \u001b[38;5;28;01mwith\u001b[39;00m \u001b[38;5;28;43mopen\u001b[39;49m\u001b[43m(\u001b[49m\u001b[38;5;124;43mf\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mdata/\u001b[39;49m\u001b[38;5;132;43;01m{\u001b[39;49;00m\u001b[43msymbol\u001b[49m\u001b[38;5;132;43;01m}\u001b[39;49;00m\u001b[38;5;124;43m_raw.csv\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mwb\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m)\u001b[49m \u001b[38;5;28;01mas\u001b[39;00m f:\n\u001b[0;32m     12\u001b[0m     f\u001b[38;5;241m.\u001b[39mwrite(response\u001b[38;5;241m.\u001b[39mcontent)\n\u001b[0;32m     14\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mData downloaded successfully!\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "File \u001b[1;32m~\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\IPython\\core\\interactiveshell.py:310\u001b[0m, in \u001b[0;36m_modified_open\u001b[1;34m(file, *args, **kwargs)\u001b[0m\n\u001b[0;32m    303\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m file \u001b[38;5;129;01min\u001b[39;00m {\u001b[38;5;241m0\u001b[39m, \u001b[38;5;241m1\u001b[39m, \u001b[38;5;241m2\u001b[39m}:\n\u001b[0;32m    304\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\n\u001b[0;32m    305\u001b[0m         \u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mIPython won\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mt let you open fd=\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mfile\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m by default \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    306\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mas it is likely to crash IPython. If you know what you are doing, \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    307\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124myou can use builtins\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m open.\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    308\u001b[0m     )\n\u001b[1;32m--> 310\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mio_open\u001b[49m\u001b[43m(\u001b[49m\u001b[43mfile\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[1;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'data/AAPL_raw.csv'"
     ]
    }
   ],
   "source": [
    "# scripts/fetch_data.py\n",
    "import requests\n",
    "import pandas as pd\n",
    "\n",
    "API_KEY = 'AH5U2MZXFN2NUXMH'  # Replace with your API key\n",
    "symbol = 'AAPL'  # or MSFT, TSLA, etc.\n",
    "\n",
    "url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&outputsize=full&apikey={API_KEY}&datatype=csv'\n",
    "\n",
    "response = requests.get(url)\n",
    "with open(f'data/{symbol}_raw.csv', 'wb') as f:\n",
    "    f.write(response.content)\n",
    "\n",
    "print(\"Data downloaded successfully!\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5be38d82-7c28-4a8e-991b-c59c32e74c62",
   "metadata": {},
   "outputs": [],
   "source": [
    "def fetch_indicator(symbol, indicator):\n",
    "    url = f\"https://www.alphavantage.co/query?function={indicator}&symbol={symbol}&interval=daily&time_period=14&series_type=close&apikey={API_KEY}&datatype=csv\"\n",
    "    df = pd.read_csv(url)\n",
    "    return df\n",
    "\n",
    "rsi_df = fetch_indicator('AAPL', 'RSI')\n",
    "macd_df = fetch_indicator('AAPL', 'MACD')\n",
    "\n",
    "# Merge with main df\n",
    "df = df.merge(rsi_df, left_on='timestamp', right_on='time', how='left').drop(columns=['time'])\n",
    "df = df.merge(macd_df, left_on='timestamp', right_on='time', how='left').drop(columns=['time'])\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
