import streamlit as st
import pandas as pd
from Conection import get_conn
from helpers import FOREIGN_KEY_field, select_element, tabel_printer

conn = get_conn()

colWriteInsert, colButtonInsert = st.columns(2)

with colWriteInsert:
    insert_animal, insert_tutor = st.columns(2)
    with insert_animal:
        Idade = st.text_input(label="Idade")
        Peso = st.text_input(label="Peso")
        Raca = st.text_input(label="Raça")
        Nome = st.text_input(label="Nome")
    with insert_tutor:
        cpf = st.selectbox('Cpf do tutor',
                           (select_element(conn,"CPF","Tutor")),
                           index=None)
    

        
with colButtonInsert:
    buttonSelectAll = st.button(label="Inserir")

if cpf == None and buttonSelectAll:
    st.write("Preencha o CPF")
else:
    if buttonSelectAll:
        cur = conn.cursor()
        cur.execute(f'INSERT INTO "Animal" ("Idade", "Peso", "Raça", "Nome") VALUES ' \
                    f'(\'{Idade}\', \'{Peso}\', \'{Raca}\', \'{Nome}\')')
        
        id_animal = FOREIGN_KEY_field(cur,"idAnimal","Animal")
        
        cur.execute(f'INSERT INTO "Possui" ("CPF", "idAnimal") VALUES ' \
                    f'(\'{cpf}\', \'{id_animal}\')')


        
        conn.commit()
        cur.close
        conn.close