import streamlit as st
import os
import sqlalchemy
import pandas as pd
import psycopg2



# Initialize connection.


@st.cache_resource
def get_cenct():
    return st.connection("postgres", type="sql")

conn = get_cenct()
Nome = "Funcionarios"
df = conn.query(f'SELECT * FROM "{Nome}";', ttl="10m")
st.dataframe(df)
conn.query