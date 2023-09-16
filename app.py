import streamlit as st
import pandas as pd
import numpy as np
#import numpy_financial as npf
from datetime import datetime, timedelta
#from PIL import Image
#import openpyxl

nome_projeto = []
naureza_projeto = []
valor_projeto = []
df = pd.DataFrame(zip(nome_projeto, naureza_projeto, valor_projeto),
                  columns = ["Nome do Projeto", "Natureza", "Valor"])
st.write(df)
