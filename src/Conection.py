import streamlit as st
import pandas as pd
import psycopg2

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
