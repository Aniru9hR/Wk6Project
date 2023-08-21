from pathlib import Path
import streamlit as st
import sys
import os

filepath = os.path.join(Path(__file__).parents[1])
print(filepath)

sys.path.insert(0, filepath)

from to_mongo import ToMongo

c = ToMongo()
st.header('Player Page')
st.write('This page will search our database for any given squad from a given football dataset you input. Spelling currently must be exact.')

answer = st.text_input('Enter a squad :', value = 'Leeds United')
st.write(list(c.player_stats.find({'squad': answer})))