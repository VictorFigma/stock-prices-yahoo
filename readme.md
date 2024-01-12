## About The Project <a id="top"></a>
A Python script that retrieves the current price and all-time high of a custom list of stocks, including crypto, from Yahoo! Finance. The script displays the data directly via console.

## Getting Started
Given that [Python 3.11+](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/) are installed and correctly configured in the system:

Install  `yfinance`  using  `pip`:
```pip install yfinance --upgrade --no-cache-dir```

## Execution
### How to execute
1. Specify the stocks you want to check in the [/data/stock_list.json](data/stock_list.json) file. You can write whatever you want in the key field, but **the value must be the exact code Yahoo uses**. 
	 ```
	 Reminder: the format is {"key1" : "value1", "key2":"value2"} 
	 Example: {"NVDIA": "NVDA", "SP500": "^GSPC"}
	 ```
2. The **all-time highs are NOT calculated by default** since it implies getting all the historical values of all the listed stocks. You can re-calculate them every time you want using the `-update` option.
	
	***2.A***  [Console] Update the all-time highs stored values and run the script afterward.
	```python3 stock-prices-yahoo.py -update``` 
	
	***2.B*** [Console] Run the script using the stored all-time highs values.
	```./stock-prices-yahoo.py```

## License
This project has been built for my personal research usage only. While I don't mind if you use it to build your own project, you must comply with  [yfinance](https://github.com/ranaroussi/yfinance), [Yahoo API](https://legal.yahoo.com/us/en/yahoo/terms/product-atos/apiforydn/index.html), and [Yahoo](https://policies.yahoo.com/us/en/yahoo/terms/index.htm) terms of use.

<p align="right">(<a href="#top">back to top</a>)</p>