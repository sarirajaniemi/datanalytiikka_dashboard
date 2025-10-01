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

Game= df["Game"]
Game

yhdistetty = pd.concat([Game,Sold],axis=1)
yhdistetty


df = pd.read_csv("ps4sales.csv")
lista = df["Game"].unique()
lista

Sold= df[["Game", "Sold"]]
Sold


#fig =plt.figure()
#plt.bar ["Game"], 
#plt.xticks(rotation=90, fontsize=5)
#st.pyplot(fig)
df = df.dropna(subset=["Game", "Sold"])
df["Sold"] = pd.to_numeric(df["Sold"], errors="coerce")

# Halutessa top-20, jotta x-akseli ei tukkeudu
top = df.sort_values("Sold", ascending=False).head(20)

# 2a) Pystypylväät
fig, ax = plt.subplots()
ax.bar(top["Game"], top["Sold"])
ax.set_xlabel("Game")
ax.set_ylabel("Sold")
plt.xticks(rotation=90, fontsize=6)
st.pyplot(fig)







