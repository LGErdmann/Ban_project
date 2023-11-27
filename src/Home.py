import streamlit as st
import pandas as pd
from Conection import get_conn
from helpers import tabel_printer, select_element
from sql_scripts import join_at_All_possui, join_at_cosulta_protocolo
conn = get_conn()

NomeTabela = st.selectbox(
                        'Verificar tabela',
                        ('Animal','Funcionario','Tutor','Consulta','Agendamento'),
                        index=None)


if NomeTabela != None:
    tabel_printer(conn,NomeTabela)
    if NomeTabela == 'Animal' or NomeTabela == 'Tutor':
        check, tabelAnimal = st.columns(2)
        with check:
            if NomeTabela == 'Animal':
                join_possui = st.checkbox('Mostrar tutores')
            if NomeTabela == 'Tutor':
                join_possui = st.checkbox('Mostrar animais')
        if join_possui:
            join_at_All_possui(conn)
   
   
    if NomeTabela == 'Consulta':
        check, tabelAnimal = st.columns(2)
        with check:
            Num = st.selectbox('Verificar tabela',
                            (select_element(conn,"NumProtocolo","Consulta")),
                            index=None
                            )

        if Num:
                join_at_cosulta_protocolo(conn,Num)

        





