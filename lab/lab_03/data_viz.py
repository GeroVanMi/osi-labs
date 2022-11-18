import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_json("data.json")
st.write(df[['date']])
st.write(df[['amountOfMails']])

fig, ax = plt.subplots()
ax.scatter(x=df[['date']], y=df[['amountOfMails']])
fig.canvas.draw()
ax.draw(fig.canvas.renderer)
# ax.set_xticklabels(ax.get_xticks(), rotation=90)
st.pyplot(fig)
