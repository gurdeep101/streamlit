#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 19:19:48 2021

@author: gurdeep_working
"""
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

image = Image.open('../data/dna-logo.jpg')

# expand the image to the width of the column
st.image(image, use_column_width=True)

st.write("""
         # DNA Nucleotide Count Web App
         
         This app counts the nucleotide composiiton of query DNA!
         
         ***
         """)
         
# input text box
# st.sidebar.header('Enter DNA sequence')
st.header('Enter DNA sequence')

# sample DNA sequence
sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

# create text box to allow user input
sequence = st.text_area("Sequence Input", sequence_input, height = 250)
sequence = sequence.splitlines() # new line on every \n character 
sequence = sequence[1:] # skips the 1st line which is the name of the sequence
sequence = ''.join(sequence) # concatenate list to string

# draw a line
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
    d = dict()
