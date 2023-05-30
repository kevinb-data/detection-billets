# AUTOGENERATED! DO NOT EDIT! File to edit: web_app.ipynb.

# %% auto 0
__all__ = []

# %% web_app.ipynb 5
import pandas as pd
import streamlit as st
from datetime import datetime


st.title("Détection de faux billets 💵")
st.markdown(
    """

Bienvenue dans l'application web simplifiée de détection de faux billets.

Cette application aide à prédire si un billet sera faux ou vrai selon ses caractéristiques.
Veuillez svp déposer le fichier CSV faire votre sélection au sein des variables en side-bar pour obtenir votre résultat.

"""
)

uploaded_file = st.sidebar.file_uploader(label="Déposez le fichier CSV 'jeu_final_predictions' ici", type = ['csv'])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, encoding='utf-8', sep=';')

else:
    st.title("⚠️ Attention, veuillez déposer un fichier")

uploaded_model = st.sidebar.file_uploader(label="Déposez le modèle ici")
model = open(uploaded_model, 'rb')

st.write(model)

st.sidebar.header("Les paramètres du billet à l'étude")

def user_input():
    

    diagonal = st.sidebar.selectbox('Diagonale du billet', options=df['diagonal'].values, index=0)
    height_left = st.sidebar.selectbox('Hauteur gauche du billet', options=df['height_left'].values, index=0)
    height_right = st.sidebar.selectbox('Hauteur droite du billet', options=df['height_right'].values, index=0)
    margin_low = st.sidebar.selectbox('Marge basse du billet', options=df['margin_low'].values, index=0)
    margin_up = st.sidebar.selectbox('Marge haute du billet', options=df['margin_up'].values, index=0)
    length = st.sidebar.selectbox('Longueur du billet', options=df['length'].values, index=0)
    
    data={
        'diagonal':diagonal,
        'height_left': height_left,
        'height_right': height_right,
        'margin_low': margin_low,
        'margin_up': margin_up,
        'length': length
    }
    
    billet_parametres=pd.DataFrame(data, index=[0])
    
    return billet_parametres

df_=user_input()


st.subheader('On veut trouver si notre billet (avec les caractéristiques suivantes) est vrai ou faux')
st.write(df_.iloc[:,0:6])

st.subheader('La prédiction du billet est:')

merged_df = df.merge(df_, on=['diagonal', 'height_left', 'height_right', 'margin_low', 'margin_up', 'length'], how='inner')
selected_columns = merged_df.iloc[:,7:11]
st.write(selected_columns)
