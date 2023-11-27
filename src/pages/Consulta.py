import streamlit as st
import pandas as pd
from Conection import get_conn
from helpers import select_element


conn = get_conn()

colWriteInsert, colButtonInsert = st.columns(2)

with colWriteInsert:
    
    NumProtocolo = st.selectbox('Qual Agendamento?',
                           (select_element(conn,"NumProtocolo","Agendamento")),
                           index=None)
    
    ObsVet = st.text_area(label="Obsevações")
    PrescVet = st.text_area(label="Prescrição")
    

with colButtonInsert:
    buttonSelectAll = st.button(label="Finalizar consulta")

if buttonSelectAll:
    cur = conn.cursor()
    cur.execute(f'INSERT INTO "Consulta" ("NumProtocolo", "ObsVet", "PrescVet") VALUES ' \
                f'(\'{NumProtocolo}\', \'{ObsVet}\', \'{PrescVet}\')')

    conn.commit()
    cur.close
    conn.close 