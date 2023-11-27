import streamlit as st
import pandas as pd
from Conection import get_conn
from helpers import select_element


conn = get_conn()

colWriteInsert, colButtonInsert = st.columns(2)

with colWriteInsert:
    
    idFunc = st.selectbox('ID Veterinário',
                           (select_element(conn,"idFunc","MedVet")),
                           index=None)
    idAnimal = st.selectbox('ID Animal',
                           (select_element(conn,"idAnimal","Animal")),
                           index=None)
    
    data = st.date_input(label="data")
    hora = st.time_input('Time', value=None)
    

with colButtonInsert:
    buttonSelectAll = st.button(label="Agendar")

if buttonSelectAll:
    cur = conn.cursor()
    cur.execute(f'INSERT INTO "Agendamento" ("idAnimal", "IdFunc", "DataAgend", "HoraAgend") VALUES ' \
                f'(\'{idAnimal}\', \'{idFunc}\', \'{data}\', \'{hora}\')')

    conn.commit()
    cur.close
    conn.close 