import streamlit as st
import numpy as np  
import pandas as pd
import matplotlib.pyplot as plt
import joblib
import io
import os

def main():

    st.title("Modello regressione lineare")
    #creare absolute path
    absolute_path = os.path.dirname(__file__)
    relative_path = "Startup_3input.pkl"
    full_path = os.path.join(absolute_path, relative_path)
    newmodel = joblib.load(full_path)
    rd = st.number_input("R&D spend", value= 0.0)
    amm = st.number_input("administration", value=0.0)
    mark = st.number_input("Marketing", value=0.0)
    res = newmodel.predict([[rd, amm, mark]])[0]
    st.write(f"Predicted profit {round(res,1)}$")


    # Parte per caricare il file CSV o Excel
    st.header("Caricamento dati")
    file = st.file_uploader("Carica un file CSV o Excel", type=["csv", "xlsx"])
    if file is not None:
        if file.type.startswith('application/vnd.openxmlformats-officedocument.spreadsheetml'):
            df = pd.read_excel(file, engine='openpyxl')
        else:
            df = pd.read_csv(file)
        dfx = df.to_numpy()
        # Mostra i dati caricati
        st.write("Dati caricati:")
        st.write(df)

        # Previsione dei dati usando il modello di regressione lineare
        st.header("Previsione dei dati")
        predictions = newmodel.predict(dfx)
        df['Predicted Profit'] = np.round(predictions, 1)
        st.write("Risultati previsione:")
        st.write(df)
        # Aggiungi un pulsante per il download del file
        output = io.BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df.to_excel(writer,sheet_name='Profit_prediction', index=False)
        writer.save()
        output.seek(0)
        st.download_button(
            label="Scarica file Excel",
            data=output,
            file_name='Profit_prediction.xlsx',
            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        st.title("Sono un coglionazzo")

if __name__ == "__main__":
    main()