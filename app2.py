import streamlit as st
import pandas as pd

# creo un dataframe di esempio
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# creo il bottone
if st.button('Resetta'):
    # chiedo conferma
    if st.warning('Sei sicuro di voler resettare il dataframe?'):
        # resetto il dataframe
        df = pd.DataFrame()

# visualizzo il dataframe
st.write(df)