import os
import json
import yfinance as yf

def get_stock_price(symbol):
    stock = yf.Ticker(symbol)
    try:
        current_price = stock.history(period='1d')['Close'].iloc[-1]
    except Exception as NotFoundException:
        current_price = -1
    return current_price

def print_all_info():
    stock_list_path = os.path.join(os.path.dirname(__file__), '../data/stock_list.json')
    with open(stock_list_path, 'r') as json_file:
        stock_list = json.load(json_file)
    max_list_path = os.path.join(os.path.dirname(__file__), '../data/max_prices.json')
    with open(max_list_path, 'r') as json_file:
        max_list = json.load(json_file)
        
    print("--------NAME-------- --------STOCK-------- --------CURRENT-------- --------HIGH--------")
    
    require_update = 0
    for name in stock_list.keys():
        try:
            stock_max = max_list[stock_list[name]]
        except Exception as NotFoundException:
            require_update = 1
            stock_max = -1
        print(f"        {name}              {stock_list[name]}                  {get_stock_price(stock_list[name]):.2f}                  {stock_max}")
    if require_update:
        print(f"Run \".\stock-prices-yahoo.py -update\" to get the missing all-time highs")