import streamlit as st
import pandas as pd
from Conection import get_conn
from helpers import FOREIGN_KEY_field

conn = get_conn()


colWriteInsert, colButtonInsert = st.columns(2)

with colWriteInsert:
    com, med = st.columns(2)
    with com:
        option = st.selectbox(
                            'Tipo de funcionário',
                            ('Comum','Veterinário'))
        
        
        Cargo = st.text_input(label="Cargo")
        Setor = st.text_input(label="Setor")
        Telefone = st.text_input(label="Telefone")
        Email = st.text_input(label="Email")
        Salario = st.number_input(label="Salário", value=None, placeholder="Salário")
        Nome = st.text_input(label="Nome")
    with med:
        if option != 'Comum':
                Turno = st.text_input(label="Turno")
                Especializacao = st.text_input(label="Especialização")


   
with colButtonInsert:
    buttonSelectAll = st.button(label="Inserir")


if buttonSelectAll:
    cur = conn.cursor()
    cur.execute(f'INSERT INTO "Funcionario" ("Cargo", "Setor", "Telefone", "Email", "Salario", "Nome") VALUES ' \
                f'(\'{Cargo}\', \'{Setor}\', \'{Telefone}\', \'{Email}\', {Salario}, \'{Nome}\')')
    

    #id_funcionario = FOREIGN_KEY_field(cur,"Funcionario")
    id_funcionario = FOREIGN_KEY_field(cur,"id","Funcionario")
    
    if option ==  'Veterinário':
        cur.execute(f'INSERT INTO "MedVet" ("idFunc", "Turno", "Especialização") VALUES ' \
        f'({id_funcionario}, \'{Turno}\', \'{Especializacao}\')')
        
        
    conn.commit()
    conn.close
    print(conn.status)