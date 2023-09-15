import streamlit as st
import pandas as pd
import openpyxl
st.title("Projetos")

resultado = pd.read_excel(r'C:\Users\lpalmeira\Videos\Streamlit\data\Analise_Teste_Saida.xlsx')
st.write(resultado)

