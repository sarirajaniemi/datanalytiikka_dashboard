import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

"PlayStation 4 pelit"

df = pd.read_csv("ps4sales.csv", sep=",")

print(df.head())

st.write("Ensimmäiset rivit" ,df.head())
 
st.write("Koko taulukko", df)
st.write("Datan kuvailua", df.describe())
st.write("Datan koko, elementtien lukumäärä", df.size)
st.write("Sarakkeiden lukumäärä", df.columns, len(df.columns))
st.write("Aksikset", df.axes)
st.write("Datatyypit", df.dtypes)
st.write("Datan muoto", df.shape)

Sold = df["Sold"]
Sold

st.write("Yhteenlaskettu myyntien määrä:", Sold.sum())












