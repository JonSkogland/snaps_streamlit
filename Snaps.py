import sqlite3
import streamlit as st


# Connect to database
con = sqlite3.connect("snaps.db")

# Make cusor??
cur = con.cursor()

# to execute
#cur.execute()


st.title("Snapselaug")

st.set_page_config(
    page_title="Snapselaug",
    page_icon="🧊",
    layout="wide",
)

def insert_snaps(navn, brygmester):
    snaps = '''INSERT INTO snaps(snapsenavn, brygger) 
                    Values(?,?)'''
    cur.execute(snaps, (navn, brygmester))
    con.commit()
    

# Indsæt hver snaps
st.header("Indtast din snaps")
with st.form("Indsæt snaps"):
    snapse_navn = st.text_input("Snapsenavn")
    brygmester = st.text_input("Brygmester")

    submitted = st.form_submit_button("Gem snaps")

if submitted:
    insert_snaps(snapse_navn, brygmester)
    st.success("Submitted")
# df som viser de indsatte snaps

