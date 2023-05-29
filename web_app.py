# AUTOGENERATED! DO NOT EDIT! File to edit: web_app.ipynb.

# %% auto 0
__all__ = []

# %% web_app.ipynb 6
import pandas as pd
import streamlit as st
from datetime import datetime


st.title("Détection de faux billets 💵")
st.markdown(
    """

Bienvenue dans l'application web simplifiée de détection de faux billets.

Cette application aide à prédire si un billet sera faux ou vrai selon ses caractéristiques.
Veuillez svp faire votre sélection au sein des variables en side-bar pour obtenir votre résultat.

"""
)

# Setup file upload
# global df
uploaded_file = st.sidebar.file_uploader(label="Upload your Excel file", type = ['csv'])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, encoding='utf-8', sep=';')
#     st.write(df)
#     st.dataframe(df,3000,500)
else:
    st.write("⚠️ Attention, pas de fichier en input")

st.sidebar.header("Les paramètres du billet à l'étude")

def user_input():
#     diagonal = st.sidebar.slider('La diagonale du billet', 171.04, 173.01, 173.01)
    diagonal = st.selectbox('la diagonale du billet', options=[df['diagonal'].values.tolist()], index=0)
#     height_left = st.sidebar.slider('La hauteur gauche du billet', 103.14, 104.88, 104.88)
#     height_right = st.sidebar.slider('La hauteur droite du billet', 102.82, 104.95, 104.95)
#     margin_low = st.sidebar.slider('La marge basse du billet', 2.98, 6.90, 6.90)
#     margin_up = st.sidebar.slider('La marge haute du billet', 2.27, 3.91, 3.91)
#     length = st.sidebar.slider('La diagonale du billet', 109.49, 114.40, 114.40)
    data={
        'diagonal':diagonal,
#         'height_left': height_left,
#         'height_right': height_right,
#         'margin_low': margin_low,
#         'margin_up': margin_up,
#         'length': length
    }
    
    billet_parametres=pd.DataFrame(data)
    
    return billet_parametres

df=user_input()

st.subheader('On veut trouver si notre billet est vrai ou faux')
st.write(df.iloc[:,0:6])


st.subheader('La prédiction du billet est:')
st.write(df.iloc[:,7:10])

# st.write(df)
