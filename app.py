import streamlit as st
import pandas as pd
import numpy as np
#import numpy_financial as npf
from datetime import datetime, timedelta
#from PIL import Image
#import openpyxl

df = pd.read_excel("Analise_Fim.xlsx")

st.title('Análise de Viabilidade de Projeto - Capex')
