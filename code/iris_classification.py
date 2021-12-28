#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 18:00:14 2021

@author: gurdeep_working
"""
import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write("""
         ## Simple Iris Flower Prediction App
         """)

# sidebar to take input
st.sidebar.header('User Input Parameters')

def user_input_features():
    # slider - label, start value, end value, default value
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal Width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal Length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal Width', 0.1, 2.5, 0.2)
    
    # define dict to take data
    data = {'sepal_length' : sepal_length,
            'sepal_width' : sepal_width,
            'petal_length' : petal_length,
            'petal_width' : petal_width
            }
    
    # convert to df
    features = pd.DataFrame(data, index = [0])
    return features

# call function to get value input from user
df = user_input_features()

# display title
st.subheader('User Input Parameters')
# display user input
st.write(df)

# load data
iris = datasets.load_iris()
x = iris.data
y = iris.target

# define and train classifier
clf = RandomForestClassifier()
clf.fit(x,y)

# run prediction on user input
prediction = clf.predict(df)

# assign prediction probabilities to a variable
prediction_proba = clf.predict_proba(df)

# display results - title and value
st.subheader('Class labels and their corresponding index number')
st.write(iris.target_names)

st.subheader('Prediction')
st.write(iris.target_names[prediction])

st.subheader('Prediction Probability')
st.write(prediction_proba)