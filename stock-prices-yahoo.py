import os
import sys
import json

if (len(sys.argv) == 2) and (sys.argv[1] == "-update"):
    print("Gathering all-time high data...")
    from scripts import update_max
    update_max.update_and_store_max()
else:
    print("STOCK ALL-TIME HIGH MAY NOT BE UP TO DATE")
    print("Run \".\stock-prices-yahoo.py -update\" to get the newest all-time high data")

from scripts import get_prices
get_prices.print_all_info()