import streamlit as st
import pandas as pd
from Conection import get_conn
from helpers import tabel_printer, FOREIGN_KEY_field
conn = get_conn()


colTetx, colButton = st.columns(2)
with colTetx:
    Nome = st.text_input(label="teste")
with colButton:
    buttonSelectAll = st.button(label="Pesquisar")

if buttonSelectAll:
    cur = conn.cursor()
    tabel_printer(cur,Nome)
    print(cur.fetchall())
    #cur.close()