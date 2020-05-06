# -*- coding: utf-8 -*-
from datetime import datetime
import json
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
from scipy.stats import norm, gmean

START_DATE = '2007-1-1'
YEARS = 40
DAYS_IN_YEAR = 253
YEARLY_SAVINGS = 1200
DAILY_SAVINGS = YEARLY_SAVINGS / DAYS_IN_YEAR
PORTFOLIO_VALUE = 1000


def get_simulation(data):
    log_returns = np.log(1 + data.pct_change())
    u = log_returns.mean()
    var = log_returns.var()
    drift = u - (0.5 * var)
    stdev = log_returns.std()
    t_intervals = DAYS_IN_YEAR * YEARS
    iterations = 10
    daily_returns = np.exp(
        drift + stdev * norm.ppf(np.random.rand(t_intervals, iterations)))
    S0 = data.iloc[-1]
    price_list = np.zeros_like(daily_returns)
    price_list[0] = S0
    for t in range(1, t_intervals):
        price_list[t] = price_list[t - 1] * daily_returns[t]

    asset_returns = price_list[-1] / (price_list[0])
    return gmean(asset_returns)


def get_data(stock):
    data = pd.DataFrame()
    if stock['type'] == 'index':
        data = wb.DataReader(stock['ticker'], 'stooq',
                             start=START_DATE)['Close']
        return get_simulation(data)
    data = wb.DataReader(stock['ticker'], 'yahoo',
                         start=START_DATE)['Adj Close']
    return get_simulation(data)


def get_expected_portfolio_return(porfolio):
    return np.sum(portfolio['weight'] * porfolio['returns'])


def get_portfolio():
    with open('portfolio.json', 'r') as portfolio_file:
        portfolio_json = portfolio_file.read()
        return json.loads(portfolio_json)['portfolio']


portfolio_data = get_portfolio()
portfolio = pd.DataFrame(portfolio_data).assign(
    returns=[get_data(stock) for stock in portfolio_data])

expected_portfolio_return = get_expected_portfolio_return(portfolio)
final_value = expected_portfolio_return * PORTFOLIO_VALUE

print('Estimated value of Portfolio in {} : £{:,.2f} \nExpected Portfolio Return: {:,.2f}%').format(
    datetime.now().year + YEARS, final_value, expected_portfolio_return * 100)
print('Estimated Income £{:,.2f}').format(final_value * 0.04)
