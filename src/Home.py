import streamlit as st
import pandas as pd
from Conection import get_conn
from helpers import tabel_printer, select_element
from sql_scripts import join_at_All_possui, join_at_cosulta_protocolo, sub_and_agr, join_at_one_possui
conn = get_conn()

col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
   st.image("logo.png")

with col3:
    st.write(' ')
NomeTabela = st.selectbox(
                        'Verificar tabela',
                        ('Animal','Funcionario','Tutor','Consulta','Agendamento','MedVet','Possui'),
                        index=None)


if NomeTabela != None:
    tabel_printer(conn,NomeTabela)
    
    if NomeTabela == 'Animal':
        check, tabelAnimal = st.columns(2)
        
        with check:
            if NomeTabela == 'Animal':
                join_possui = st.checkbox('Mostrar tutores')

        if join_possui:
            coljoin, colcpf = st.columns(2)
            
            with coljoin:
                     join_at_All_possui(conn)
            with colcpf:
                    cpf = st.selectbox('Filtrar por CPF',
                                    (select_element(conn,"CPF","Tutor")),
                                    index=None
                                    )
            
            if cpf:

                join_at_one_possui(conn,cpf)

            
   
   
    if NomeTabela == 'Consulta' or NomeTabela == 'Agendamento':
        check, tabelAnimal = st.columns(2)
        
        with check:
            Num = st.selectbox('Verificar Protocolo',
                            (select_element(conn,"NumProtocolo","Consulta")),
                            index=None
                            )

        if Num:
                join_at_cosulta_protocolo(conn,Num)

    if NomeTabela == 'Funcionario':
        check, tabelAnimal = st.columns(2)
        sub = st.checkbox('Funcionário com maior salário')
        
        with check:
            if sub:
                sub_and_agr(conn)
            

    

        





