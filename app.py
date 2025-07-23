# arquivo: app.py
import streamlit as st
import re

def limpar_cpf(cpf):
    return re.sub(r'\D', '', cpf)

st.title("Limpador de CPF")

cpf_input = st.text_input("Digite o CPF com pontos ou traço:")

if st.button("Limpar CPF"):
    cpf_limpo = limpar_cpf(cpf_input)
    st.success(f"CPF limpo: {cpf_limpo}")
