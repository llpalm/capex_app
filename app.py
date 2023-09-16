import streamlit as st
import pandas as pd
import numpy as np
#import numpy_financial as npf
from datetime import datetime, timedelta
#from PIL import Image
#import openpyxl

nome_projeto = []
naureza_projeto = []
diretoria_projeto = []
df = pd.DataFrame(zip(nome_projeto, naureza_projeto, diretoria_projeto),
                  columns = ["Nome do Projeto", "Natureza", "Diretoria"])

st.write(df)

#st.set_page_config (page_title="Modelagem Financeira Capex", layout='wide')
st.title('Análise de Viabilidade de Projeto - Capex')
# Configuração da página 
#st.set_page_config (page_title="Modelagem Financeira Capex" )
st.title('Cadastro')

st.sidebar.success('Menu de Navegação')


with st.form(key='Cadastrar'):
    nome_projeto = st.text_input('Nome do Projeto')
    col1,col2, col3 = st.columns(2)
    with col1:
        natureza = st.selectbox(label='Natureza', options=['Modernização', 'Expansão'])
    with col2:   
        diretoria = st.selectbox(label='Diretoria', options=['Florestal', 'Celulose', 'Papel'])

    add_suporte = st.form_submit_button('Cadastrar')
    if add_suporte:
        #st.write(nome_projeto, natureza)
        new_add_suporte = {'Nome do Projeto': nome_projeto, 'Natureza': natureza}
        suporte = suporte.append(new_add_suporte, ignore_index=True)
        #st.write(suporte)

