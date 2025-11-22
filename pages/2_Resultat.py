import sqlite3
import streamlit as st
import pandas as pd
import altair as alt

def display_vinder(df):
    sorted = df.sort_values(by=["value"], ascending=False)
    max = sorted.head(1).reset_index()
    bedste = max["brygger"]
    st.header(f"Brygmester: {bedste[0]}")
    st.balloons()

# Connect to database
con = sqlite3.connect("snaps.db")

# Make cusor??
cur = con.cursor()

# Data retrieval
data = cur.execute("SELECT * FROM votering JOIN snaps ON snaps.SnapsID = votering.SnapsID")
df = pd.DataFrame(data.fetchall())
df.columns = [description[0] for description in cur.description]

# Wrangling
df = df.drop(columns=["stemmeid"])
df = df.drop(df.columns[11], axis=1)
categories = df.drop(columns=["snapsenavn", "brygger", "dommer"])
summed_df = df.groupby(["snapsenavn"]).sum().reset_index()
melted = pd.melt(summed_df, id_vars=["snapsenavn", "dommer", "brygger"])

summed = melted.groupby(["snapsenavn", "brygger"]).sum(["value"])

# # Charting
# chart = (
#     alt.Chart(melted)
#     .mark_bar()
#     .encode(
#         x="snapsenavn", 
#         y="value:Q", 
#         color="variable"
#     )
#)

tab1, tab2, tab3, tab4 = st.tabs(["Overall", "Damage", "Smag", "Vibe"])

#st.altair_chart(chart)
with tab1:
    display_vinder(summed)
    st.bar_chart(summed_df, x="snapsenavn", y=categories.columns)
    st.dataframe(summed)

with tab2:
    st.header("Mest damage")




