import streamlit as st
import pandas as pd
from Conection import get_conn
from helpers import tabel_printer, FOREIGN_KEY_field
from sql_scripts import join_at_All_possui
conn = get_conn()

NomeTabela = st.selectbox(
                        'Verificar tabela',
                        ('Animal','Funcionario','Tutor','Consulta','Agendamento'),
                        index=None)


if NomeTabela != None:
    if NomeTabela == 'Animal' or NomeTabela == 'Tutor':
        tabel_printer(conn,NomeTabela)
        check, tabelAnimal = st.columns(2)
        with check:
            if NomeTabela == 'Animal':
                join_possui = st.checkbox('Mostrar tutores')
            if NomeTabela == 'Tutor':
                join_possui = st.checkbox('Mostrar animais')
        if join_possui:
            join_at_All_possui(conn)
    else:
        tabel_printer(conn,NomeTabela)
        #print(cur.fetchall())
        #cur.close()
        
        





