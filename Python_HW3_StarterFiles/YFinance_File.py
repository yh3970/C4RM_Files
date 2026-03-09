import numpy as np
import pandas as pd

def YahooData2returns(YahooData=None, symbol='AAPL'):
    # Input:
    # YahooData = data from Yahoo Finance
    # Output:
    # returns = array of returns

    # Extract the Close prices for the chosen symbol
    close_prices = YahooData[('Close', symbol)].to_numpy()

    # Calculate simple lagged returns
    returns = close_prices[1:] / close_prices[:-1] - 1

    return returns
