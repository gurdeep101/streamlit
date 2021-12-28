# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 15:40:49 2021

@author: gurdeep.singh
"""
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier

# title in markdown format
st.write("""
#Penguin Prediction App
       
This app predicts the **Palmer Penguin** species!

Data obtained from the [palmerpenguins library](https://github.com/allisonhorst/palmerpenguins) in R by Allison Horst.
         """)

st.sidebar.header('User Input Features')

# sample file for download
st.sidebar.markdown("""
[Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/penguins_example.csv)
                    """)
                    
# file upload or input using slider bar and dropwdown
# predictions made using data input from either methods above

# option for user to upload file
uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type = ["csv"])

if uploaded_file is not None:
    # store user uploaded data from csv into input_df
    input_df = pd.read_csv(uploaded_file)
else:
    def user_input_features():
        # function for slidebar and dropdown to input data
        # take in data
        island = st.sidebar.selectbox('Island', ('Biscoe', 'Dream', 'Torgersen'))
        sex = st.sidebar.selectbox('Sex',('Male', 'Female'))
        bill_length_mm = st.sidebar.slider('Bill length(mm)', 32.1, 59.6, 43.9) # min, max, current
        bill_depth_mm = st.slidebar.slider('Bill length(mm)', 13.1, 21.5, 17.2) # min, max, current
        flipper_length_mm = st.slidebar.slider('Flipper Length(mm)', 172.0, 231.0, 201.0)
        body_mass_g = st.slidebar.slider('Body Mass (g)', 2700.0, 6300.0, 4207.0)
        
        # data input into dataframe
        data = {'island': island,
                'bill_length': bill_length_mm,
                'bill_depth': bill_depth_mm,
                'flipper_length': flipper_length_mm,
                'body_mass_g': body_mass_g,
                'sex': sex
                }
        features = pd.DataFrame(data, index = [0])
        return features
    # store user input data as input_df
    input_df = user_input_features()
    
# combines user input features with entire penguins dataset
# this will be useful for encoding phase; since encoding needs options and user input may only be 1
penguins_raw = pd.read_csv('penguins_cleaned.csv')
penguins = penguins_raw.drop(columns = ['species'])
df = pd.concat([input_df, penguins], axis =  0) # row wise combine

# encoding of ordinal features
# # https://www.kaggle.com/pratik1120/penguin-dataset-eda-classification-and-clustering
encode = ['sex', 'island']
for col in encode:
    dummy = pd.get_dummies(df[col], prefix=col)
    df = pd.concat([df,dummy], axis=1)
    del df[col]
df = df[:1] # Selects only the first row (the user input data)

# Displays user input features
st.subheader('User Input Features')

if uploaded_file is not None:
    st.write(df)
else:
    st.write("CSV not uploaded, Currently using sample parameters below")
    st.write(df)
    
# read in saved classification model
load_clf = pickle.load(open('penguins_clf.pkl', 'rb'))

# apply model to make predictions
predictions = load_clf.predict(df)
predictions_proba = load_clf.predict_proba(df)

st.subheader('Prediction')
penguins_species = np.array(['Adelie', 'Chinstrap', 'Gentoo'])
st.write(penguins_species[predictions])

st.subheader('Prediction Probability')
st.write(predictions_proba)