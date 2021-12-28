#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 18:41:42 2021

@author: gurdeep_working
"""
import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import yfinance as yf

st.title('S&P 500 App')

st.markdown("""
This app retrieves the list of the **S&P500** from wikipedia and its corresponding **stock** prices
* **Data source:** [Wikipedia](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies).
        """)
        
st.sidebar.header('User Input Features')

# web scraping of SP500 data from wikipedia
@st.cache # data downloaded and stored in cache
def load_data():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    # reads table form url; header = 0 --> 1st table only
    html = pd.read_html(url, header= 0)
    df = html[0]
    return df

df = load_data()
sector = df.groupby('GICS Sector')

# Sidebar - Sector Selection
# get unique values for sector and sort
# show shorted results as multiselect bar
sorted_sector_unique = sorted(df['GICS Sector'].unique())
selected_sector = st.sidebar.multiselect('Sector', sorted_sector_unique, sorted_sector_unique)

# filtering data
df_selected_sector = df[df['GICS Sector'].isin(selected_sector)]

st.header('Display Companies in Selected Sector')
st.write('Data Dimension: ' + str(df_selected_sector.shape[0]) + ' rows and ' +
         str(df_selected_sector.shape[1]) + ' columns.')

st.dataframe(df_selected_sector)

# make S&P 500 list of companies available to download
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
def filedownload(df):
    csv = df.to_csv(index = False)
    b64 = base64.b64encode(csv.encode()).decode() # strings <-> bytes conversion
    # insert hyperlink
    href = f'<a href="data:file/csv;base64,{b64}" download="SP500.csv">Download CSV File</a>'
    return href

st.markdown(filedownload(df_selected_sector), unsafe_allow_html=True)

# download stock prices using yfinance - for 1st 10 companies in selected sector
data = yf.download(
    tickers = list(df_selected_sector[:10].Symbol),
    period = "ytd",
    interval = "1d",
    group_by = 'ticker',
    auto_adjust = True,
    prepost = True,
    threads = True,
    proxy = None
    )

# plot closing price of symbol queried
def price_plot(symbol):
    df = pd.DataFrame(data[symbol].Close)
    df['Date'] = df.index
    plt.fill_between(df.Date, df.Close, color = 'skyblue')
    plt.plot(df.Date, df.Close, color =  'skyblue')
    plt.xticks(rotation=90)
    plt.title(symbol, fontweight = 'bold')
    plt.xlabel('Date', fontweight = 'bold')
    plt.ylabel('Closing Price', fontweight = 'bold')
    return st.pyplot()

num_company = st.sidebar.slider('Number of companies', 1, 5)

# show plots if option selected
if st.button('Show Plots'):
    st.header('Stock Closing Price')
    for i in list(df_selected_sector.Symbol)[:num_company]:
        price_plot(i)









