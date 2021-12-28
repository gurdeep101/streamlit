#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 12:00:36 2021

@author: gurdeep_working
"""
import streamlit as st
from PIL import Image
import pandas as pd
import base64
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import json
import time

# page layout - page expands to full width
st.set_page_config(layout='wide')

# title
image = Image.open('../data/logo.jpg')
st.image(image, width = 500)
st.title('Crypto Price App')
st.markdown("""This app retreieves cryptocurrency prices for the top 100 
            cryptocurrencies from the **CoinMarketCap**!!""")

# About (Displays the "+" sign in the app to show below text)
expander_bar = st.beta_expander("About")
expander_bar.markdown("""
    * **Python Libraries:*** 
    * **Data Source:** coinmarketcap.com
    * **Credit:** Web scraping crypto prices with Python Medium
                      """)

# Page Layout
# Divide page into 3 columns col1 = sidebar, col2 and col3 = page contents
col1 = st.sidebar
col2, col3 = st.beta_columns((2,1))

col1.header('Input Options')

# sidebar currency price unit
currency_price_unit = col1.selectbox('Select currency for price',('USD', 'BTC','ETH'))

# web scraping of CoinMarketCap data
@st.cache # download data and store in cache
def load_data():
    cmc = requests.get('https://coinmarketcap.com')
    soup = BeautifulSoup(cmc.content, 'html.parser')
    data = soup.find()


























