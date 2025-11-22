import streamlit as st
import sqlite3 as db


st.header("Votering")

con = db.connect("snaps.db")

# Make cusor??
cur = con.cursor()


def insert_votering(id, dommer, categories):
    æstetik, initialsmag, eftersmag, zoink, præsentation, kreativitet, edikette, dunst, damage = categories.values() 
    sql = '''INSERT INTO votering(SnapsID, æstetik, initialsmag, eftersmag, zoink, præsentation, kreativitet, edikette, dunst, damage, dommer)
             VALUES(?,?,?,?,?,?,?,?,?,?,?)'''
    cur.execute(sql, (id, æstetik, initialsmag, eftersmag, zoink, præsentation, kreativitet, edikette, dunst, damage, dommer))
    con.commit()


with st.form("Vurdering"):
    ## Skal hente snaps fra databasen
    data = cur.execute("SELECT SnapsID, snapsenavn FROM snaps")
    rows = data.fetchall()
    snaps_liste = [row[1] for row in rows]
    valgte_snaps = st.selectbox("Vælg den snaps du vil vurdere", snaps_liste, accept_new_options=False)
    
    snaps_id = 0
    for row in rows:
        if row[1] == valgte_snaps:
            snaps_id = row[0]

    dommer = st.text_input("Dommer", placeholder="dit navn")

    categories = {"Æstetik": 0,
        "Initalsmag": 0,
        "Eftersmag": 0,
        "Zoink": 0,
        "Præsentation": 0,
        "Kreativitet": 0,
        "Edikette": 0,
        "Dunst": 0,
        "Damage": 0,
    }

    for key, value in categories.items():
        categories[key] = st.number_input(key, min_value=1, max_value=5, step=1, value=None, placeholder=0)

    submitted = st.form_submit_button()


if submitted:
    if any(v is None for v in categories.values()):
        st.error("All categories must be filled out before submitting.")
    else:
        insert_votering(snaps_id, dommer, categories)
        st.success("Submitted")