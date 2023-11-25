import streamlit as st
import pandas as pd
import psycopg2

# Initialize connection.
@st.cache_resource
def get_conn():
    conn = psycopg2.connect(
        host='localhost',
        port='5432',
        database='postgres',
        user='postgres',
        password='postgres'
    )
    return conn

conn = get_conn()

colTetx, colButton = st.columns(2)
with colTetx:
    Nome = st.text_input(label="teste")
with colButton:
    buttonSelectAll = st.button(label="Pesquisar")

if buttonSelectAll:
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM "{Nome}"')
    results = cur.fetchall()
    st.dataframe(results)
    cur.close()


colWriteInsert, colButtonInsert = st.columns(2)

with colWriteInsert:
    Cargo = st.text_input(label="Cargo")
    Setor = st.text_input(label="Setor")
    Telefone = st.text_input(label="Telefone")
    Email = st.text_input(label="Email")
    Salario = st.number_input(label="Salário", value=None, placeholder="Sálario")
    Nome = st.text_input(label="Nome")
    _returnData = [Cargo, Setor, Telefone, Email, Salario, Nome]
with colButtonInsert:
    buttonSelectAll = st.button(label="Inserir")


if buttonSelectAll:
    cur = conn.cursor()
    cur.execute(f'INSERT INTO "Funcionarios" ("Cargo", "Setor", "Telefone", "Email", "Salário", "Nome") VALUES ' \
            f'(\'{Cargo}\', \'{Setor}\', \'{Telefone}\', \'{Email}\', {Salario}, \'{Nome}\')')
    cur.close