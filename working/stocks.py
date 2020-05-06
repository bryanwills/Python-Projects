import numpy as nup
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

stocks = [
    {
        'ticker': 'UU.L',
        'name': 'United Utilities',
    },
    {
        'ticker': 'VOD.L',
        'name': 'Vodafone Group',
    },
    {
        'ticker': 'BP.L',
        'name': 'BP Group',
    }

]


def create_plots(stocks):
    data = pd.DataFrame()
    for stock in stocks:
        data[stock['ticker']] = wb.DataReader(
            stock['ticker'], data_source='yahoo', start='2007-1-1')['Adj Close']
    print(data)


create_plots(stocks)
