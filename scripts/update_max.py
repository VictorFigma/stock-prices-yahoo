import os
import json
import yfinance as yf

def get_max_historical_value(symbol):
    stock_data = yf.download(symbol, period="max")
    max_value = stock_data['Close'].max()
    return round(max_value, 2)

def update_and_store_max():
    data = {}

    file_path = os.path.join(os.path.dirname(__file__), '../data/stock_list.json')
    with open(file_path, 'r') as json_file:
        stock_list = json.load(json_file)
    for value in stock_list.values():
        data[value] = get_max_historical_value(value)

    file_path = os.path.join(os.path.dirname(__file__), '../data/max_prices.json')
    with open(file_path, 'w') as json_file:
        json_file.write(json.dumps(data))

    print("All-time high data successfully gathered.")