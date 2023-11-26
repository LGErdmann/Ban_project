import streamlit as st
import pandas as pd
import psycopg2
from helpers import name_field


def join_at_All_possui(conn):
    cur = conn.cursor()
    cur.execute(  
        'SELECT t."CPF",t."Nome", a."idAnimal", a."Nome"'
        ' FROM "Tutor" as t'
        ' JOIN "Possui" ON t."CPF" = "Possui"."CPF"'
        ' JOIN "Animal" AS a ON a."idAnimal" = "Possui"."idAnimal"'
    )
    #columns = name_field(cur)
    df = cur.fetchall()
    Tabela = pd.DataFrame(df, columns=['CPF Tutor','Nome Tutor','ID Pet','Nome Pet' ])
    cur.close()
    return st.dataframe(Tabela)



def join_at_All(cur,nomePrincipal,nome2,idPrincipla,id2):
    cur.execute(   
        f'SELECT *'
        f'FROM "{nomePrincipal}"'
        f'JOIN "{nome2}" ON "{nomePrincipal}"."{idPrincipla}" = "{nome2}"."{idPrincipla}"'
        f'JOIN possui ON animal.id_animal = possui.id_animal;'
        )