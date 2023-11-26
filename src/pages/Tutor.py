import streamlit as st
import pandas as pd
from Conection import get_conn


conn = get_conn()

colWriteInsert, colButtonInsert = st.columns(2)

with colWriteInsert:
    CPF = st.text_input(label="CPF")
    Email = st.text_input(label="Email")
    Endereco = st.text_input(label="Endereço")
    Nome = st.text_input(label="Nome")
    Telefone = st.text_input(label="Telefone")

with colButtonInsert:
    buttonSelectAll = st.button(label="Inserir")

if buttonSelectAll:
    cur = conn.cursor()
    cur.execute(f'INSERT INTO "Tutor" ("CPF", "Email", "Endereço", "Nome", "Telefone") VALUES ' \
                f'(\'{CPF}\', \'{Email}\', \'{Endereco}\', \'{Nome}\', \'{Telefone}\')')

    conn.commit()
    cur.close
    conn.close 