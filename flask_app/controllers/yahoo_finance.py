from flask import render_template, request, redirect, session
from flask_app.models.login_model import User
from flask_app.models.address_model import Address
from flask_app.models.account_model import Account
from flask_app import app
import yfinance as yf
import pandas as pd

@app.route('/yahoo_test')
def yahoo_test():
    ticker=["MSFT","GOOGL", "AMZN", "AAPL", "TSLA", "COIN", "AG", "DG","SAVA" ]

    result = []
    for tk in ticker:
        data = yf.Ticker(tk).info
        # print(data)
        ticker_data = {
            "symbol": data['symbol'],
            "day_high": data['dayHigh'],
            "day_low": data['dayLow'],
            "short_name": data['shortName'],
            "earnings_growth": data['earningsGrowth']
        }
        result.append(ticker_data)

    # print(msft.info)
    # print(googl.info)
    # print(amazon.info)
    return result

@app.route('/stock_graph')
def stock_graph(request):
    # stock = request["data"]["symbol"]
    stock_data = yf.Ticker("MSFT").history(period="1mo")
    legend = 'Daily Price Tracking'
    values = stock_data["Close"].to_list()
    # Close is the column, stock_data is all the data. Data is a dataframe
    labels = [str(pd.to_datetime(stock_date).date()) for stock_date in stock_data.index]
    #labels is the index. Research list comprehension. str typecasts to a string format
    return legend, values, labels


    
