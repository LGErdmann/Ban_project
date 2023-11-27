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



def join_at_cosulta_protocolo(conn,Num):
    cur = conn.cursor()
    cur.execute(  
        'SELECT c."NumProtocolo", a."idAnimal", t."CPF" AS "CPF do Tutor", ag."DataAgend"'
        ' FROM "Consulta" c'
        ' JOIN "Agendamento" ag ON c."NumProtocolo" = ag."NumProtocolo"'
        ' JOIN "Animal" a ON ag."idAnimal" = a."idAnimal"'
        ' JOIN "Possui" p ON a."idAnimal" = p."idAnimal"'
        ' JOIN "Tutor" t ON p."CPF" = t."CPF"'
        f' WHERE c."NumProtocolo" = {Num}'
    )
    df = cur.fetchall()
    Tabela = pd.DataFrame(df, columns=['Numero de protocolo','ID Pet','CPF do tutor','Data agendamento'])
    cur.close()
    return st.dataframe(Tabela)

def sub_and_agr(conn):
    cur = conn.cursor()
    cur.execute(
        'SELECT "id", "Nome", "Salario" FROM "Funcionario" WHERE "Salario" = (SELECT MAX("Salario") FROM "Funcionario")'
        )
    df = cur.fetchall()
    Tabela = pd.DataFrame(df,columns=['idFuncionário','Nome Funcionario','Salário'])
    cur.close()
    return st.dataframe(Tabela)
