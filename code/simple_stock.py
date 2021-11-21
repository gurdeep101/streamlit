# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import yfinance as yf
import streamlit as st
import pandas as pd

# hash in st.write indicates large text
st.write("""
         # Simple Stock App
         
         Shown are the stock **closing** price and ***volume*** of Google!
         """)

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75

# define the ticker symbol
tickerSymbol = 'GOOGL'

# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# get historical prices for this ticker
tickerDF = tickerData.history(period='1d', start='2010-05-31', end = '2020-05-31')
# returns OHLC, Vol, Div, StockSplits

st.write("""
         ## Closing Price
         """)
         
st.line_chart(tickerDF.Close)
st.write("""
         ## Volume Price""")
         
st.line_chart(tickerDF.Volume)
