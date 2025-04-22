import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Clientes cadastrados",
    page_icon="🧾"
)

dados = pd.read_csv("clientes.csv")

st.title("Clientes cadastrados")
st.divider()

st.dataframe(dados)