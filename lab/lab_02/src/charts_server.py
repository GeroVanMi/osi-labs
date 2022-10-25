import streamlit as st
import pandas as pd

df = pd.read_csv('./data_filtered.csv')

st.line_chart(df, x='DATUM', y='VELO_IN')
st.write(df)
