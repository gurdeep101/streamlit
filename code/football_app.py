#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 17:34:50 2021

@author: gurdeep_working
"""
import pandas as pd
import streamlit as st
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title('NFL Football Stats (Rushing) Explorer')

st.markdown("""
   This app performs simple webscraping of NFL Football player stats data
   * **Python Libraries:** base64, pandas, streamlit, numpy, matpltlib, seaborn
   * **Data Source: [pro-football-reference.com](https://www.pro-football-reference.com/)         
            """)

st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(1990, 2020))))

# web scraping
@st.cache
def load_data(year):
    url = "https://www.pro-football-reference.com/years/" + str(year) + "/rushing.htm"
    html = pd.read_html(url, header = 1)
    # drop headers and redundant columns
    df = html[0]
    raw = df.drop(df[df.Age == 'Age'].index) # deletes repeating headers in context
    raw = df.fillna(0)
    playerstats = raw.drop(['Rk'], axis = 1)
    return playerstats

playerstats = load_data(selected_year)

# sidebar - team selection
# list of teams sorted
sorted_unique_team = sorted(playerstats.Tm.unique())
selected_team = st.sidebar.multiselect('Team', sorted_unique_team, sorted_unique_team)

# sidebar - position selection
unique_pos = ['RB', 'QB', 'WR', 'FB', 'TE']
selected_pos = st.sidebar.multiselect('Position', unique_pos, unique_pos)

# filtering data
# filter data for chosen team and position
df_selected_team = playerstats[(playerstats.Tm.isin(selected_team)) & (playerstats.Pos.isin(selected_pos))]

st.header('Display Player Stats of selected Team(s)')
st.write('Data Dimension: ' + str(df_selected_team.shape[0]) + ' rows and ' + str(df_selected_team.shape[1]) + ' columns.')
st.dataframe(df_selected_team)

# Download NFL Player Stats data
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
def filedownload(df):
    csv = df.to_csv(index = False)
    b64 = base64.b64encode(csv.encode()).decode() # strings to bytes conversions
    # insert hyperlink
    href = f'<a href="data:file/csv;base64{b64}" download="playerstats.csv">Download CSV file</a>'
    return href

st.markdown(filedownload(df_selected_team), unsafe_allow_html=True)

# heatmap
if st.button('Intercorrelation Heatmap'):
    st.header('Intercorrelation Matrix Heatmap')
    df_selected_team.to_csv('output.csv', index = False)
    df = pd.read_csv('output.csv')
    
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

    
































