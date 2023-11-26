import streamlit as st
import pandas as pd
import psycopg2

def name_field(cur):
    field_names = [i[0] for i in cur.description]
    return field_names 

def tabel_printer(cur,Nome):
    cur.execute(f'SELECT * FROM "{Nome}"')
    columns = name_field(cur)
    df = cur.fetchall()
    Tabela = pd.DataFrame(df, columns=columns)
    return st.dataframe(Tabela)

def FOREIGN_KEY_field(cur,id,Nome):
    cur.execute(f'SELECT * FROM "{Nome}" ORDER BY "{id}" DESC LIMIT 1')
    
    key = cur.fetchone()[0]

    return key


def select_element(conn,element,nome):
    
    cur = conn.cursor()
    cur.execute(f'SELECT "{element}" FROM "{nome}"')
    columns = name_field(cur)
    df = cur.fetchall()
    cur.close
    Tabela = pd.DataFrame(df, columns=columns)
    elementor = Tabela[element].tolist()
        
    return elementor