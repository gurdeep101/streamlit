#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 19:19:48 2021

@author: gurdeep_working
"""
import pandas as pd
import streamlit as st
import altair as alt # graph
from PIL import Image # display logo

# create variable image
image = Image.open('../data/dna-logo.jpg')

# display image
# expand the image to the width of the column
st.image(image, use_column_width=True)

# print header and short explanation
# 3 asterix for horizontal line
st.write("""
         # DNA Nucleotide Count Web App
         
         This app counts the nucleotide composiiton of query DNA!
         
         ***
         """)
         
# create input text box
# st.sidebar.header('Enter DNA sequence')
st.header('Enter DNA sequence')

# sample DNA sequence
sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

# create text box to allow user input; specify height of text box
sequence = st.text_area("Sequence Input", sequence_input, height = 250)
sequence = sequence.splitlines() # splits into list and inserts new line on every \n character 
sequence = sequence[1:] # skips the 1st line which is the name of the sequence
sequence = ''.join(sequence) # concatenate list to string to create long DNA sequence ready for analysis

# draw a line
# 3 asterix for horizontal line
st.write("""
         ***
         """)

# print the input DNA sequence
st.header('INPUT (DNA Query) Received')         
sequence

# DNA nucleotide count
st.header('OUTPUT (DNA Nucleotide Count')

# 4 ways to display output

# 1. Print Dictionary
st.subheader('1. Print Dictionary')

def dna_nucleotide_count(seq):
    """
    use count function to count characters
    create dictionary with count of the nucleotide
    """
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C'))
        ])
    return d

x = dna_nucleotide_count(sequence)

x

# 2. print text
st.subheader('2. Print text')
st.write('There are ' + str(x['A']) + ' adenine (A)')
st.write('There are ' + str(x['T']) + ' thymine (T)')
st.write('There are ' + str(x['G']) + ' guanine (G)')
st.write('There are ' + str(x['C']) + ' cytosine (C)')

# 3. Display dataframe
st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(x, orient = 'index')
print(df)
df = df.rename({0: 'count'}, axis = 'columns')
print(df)
df.reset_index(inplace = True)
df = df.rename(columns = {'index' : 'nucleotide'})
print(df)
st.write(df)

# 4. Display bar chart using Altair library
st.subheader('4. Display Bar Chart')

p = alt.Chart(df).mark_bar().encode(
    x = 'nucleotide',
    y = 'count'
)
p = p.properties(
    width = alt.Step(80) # controls width of the bar
)

st.write(p)



















