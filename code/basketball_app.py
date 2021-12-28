#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 16:56:10 2021

@author: gurdeep_working
"""
import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title('NBA Player Stats Explorer')

st.markdown("""
This app performs simple webscraping of NBA Player Stats data!
* **Python libaries:** base64, pandas, streamlit
* **Data Source:** [Basketball-reference.com](https://www.basketball-reference.com/)
            """)

st.sidebar.header('User Input Features')
# selectbox for including dropdown
selected_year = st.sidebar.selectbox('Year', list(reversed(range(1950, 2020))))

# web scraping of NBA Player Stats
@st.cache
def load_data(year):
    url = "https://www.basketball-reference.com/leagues/NBA_" + str(year) + "_per_game.html"
    html = pd.read_html(url, header = 0)
    df = html[0]
    raw = df.drop(df[df.Age == 'Age'].index) # Deletes repeating headers in content
    raw = raw.fillna(0)
    playerstats = raw.drop(['Rk'], axis=1)
    return playerstats

playerstats = load_data(selected_year)

# sidebar - team selection
# get alphabetically sorted list of unique players
sorted_unique_team = sorted(playerstats.Tm.unique())
selected_team = st.sidebar.multiselect('Team', sorted_unique_team, sorted_unique_team)

# sidebar - position selection
unique_pos = ['C', 'PF', 'SF', 'PG', 'SG']
selected_pos = st.sidebar.multiselect('Position', unique_pos, unique_pos)

# filtering data - based on inputs selected in sidebar
df_selected_team = playerstats[(playerstats.Tm.isin(selected_team)) & (playerstats.Pos.isin(selected_pos))]

st.header('Display player stats of selected teams')
st.write('Data Dimension: ' + str(df_selected_team.shape[0]) + ' rows and ' + str(df_selected_team.shape[1]) + ' columns.')
# display dataframe
st.dataframe(df_selected_team)

# dowload NBA Player stats data
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806

def filedownload(df):
    # create file to download CSV
    csv = df.to_csv(index = False)
    b64 = base64.b64encode(csv.encode()).decode() # converts strings to bytes
    # insert hyperlink
    href = f'<a href="data:file/csv;base64{b64}" download = "playerstats.csv">Download CSV File</a>'
    return href

# display link in app
st.markdown(filedownload(df_selected_team), unsafe_allow_html=True)

# Heatmap
# display only if button selected
if st.button('Intercorrelation Heatmap'):
    st.header('Intercorrelation Matrix Heatmap')
    # store to csv and read it back
    df_selected_team.to_csv('output.csv', index = False)
    df = pd.read_csv('output.csv')
    
    # create correlation matrix
    corr = df.corr()
    # create an array of zeros with same shape as given array
    mask = np.zeros_like(corr)
    # mask upper half of correlation matrix
    mask[np.triu_indices_from(mask)] = True
    
    # plot
    with sns.axes_style("white"):
        f, ax = plt.subplots(figsize = (7,5))
        ax = sns.heatmap(corr, mask = mask, vmax = 1, square = True)
    st.pyplot()

























