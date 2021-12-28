# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 10:09:45 2021

@author: gurdeep.singh
"""
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

df0 = pd.read_csv('../../data/penguins_cleaned.csv')

# Ordinal feature encoding
# https://www.kaggle.com/pratik1120/penguin-dataset-eda-classification-and-clustering
df = df0.copy()
target = 'species' # predict species of the penguin
encode = ['sex', 'island']

# convert categorical values to dummy features
for col in encode:
    dummy = pd.get_dummies(df[col], prefix = col)
    df = pd.concat([df, dummy], axis = 1)
    del df[col]

# convert target species into dummy variables    
target_mapper = {'Adelie' : 0, 'Chinstrap' : 1, 'Gentoo' : 2}

def target_encode(val):
    return target_mapper[val]

df['species'] = df['species'].apply(target_encode)

# separate x and y
x = df.drop('species', axis = 1)
y = df['species']

# build random forest model
clf = RandomForestClassifier()
clf.fit(x,y)

# save the model; create file and save 
pickle.dump(clf, open('penguins_clf.pkl', 'wb'))