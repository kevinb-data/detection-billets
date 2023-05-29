# AUTOGENERATED! DO NOT EDIT! File to edit: web_app.ipynb.

# %% auto 0
__all__ = []

# %% web_app.ipynb 4
from datetime import datetime

import streamlit as st

# from streamlit_jupyter import StreamlitPatcher, tqdm

# %% web_app.ipynb 5
st.title("Détection de faux billets 💵")

# %% web_app.ipynb 6
st.markdown(
    """

Bienvenue dans l'application web simplifiée de détection de faux billets.

Cette application aide à prédire si un billet sera faux ou vrai selon ses caractéristiques.
Veuillez svp faire votre sélection au sein des variables en side-bar pour obtenir votre résultat.

"""
)

# %% web_app.ipynb 7
st.sidebar.header("Les paramètres du billet à l'étude")

# %% web_app.ipynb 8
def user_input():
    diagonal = st.sidebar.slider('La diagonale du billet', 171.04, 173.01, 173.01)
    height_left = st.sidebar.slider('La hauteur gauche du billet', 103.14, 104.88, 104.88)
    height_right = st.sidebar.slider('La hauteur droite du billet', 102.82, 104.95, 104.95)
    margin_low = st.sidebar.slider('La marge basse du billet', 2.98, 6.90, 6.90)
    margin_up = st.sidebar.slider('La marge haute du billet', 2.27, 3.91, 3.91)
    length = st.sidebar.slider('La diagonale du billet', 109.49, 114.40, 114.40)
    data={
        'diagonal':diagonal,
        'height_left': height_left,
        'height_right': height_right,
        'margin_low': margin_low,
        'margin_up': margin_up,
        'length': length
    }
    
    billet_parametres=pd.DataFrame(data,index=[0])
    
    return billet_parametres

df=user_input()

st.subheader('On veut trouver si notre billet est vrai ou faux')
st.write(df)

st.subheader('La prédiction du billet est:')
st.write(dataframe[''])
