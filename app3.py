import streamlit as st
import pandas as pd
import base64

def add_rows(df):
    for idx, _ in enumerate(df.index):
        st.write(f"Riga {idx + 1}")
        row = {}
        for col in df.columns:
            value = st.text_input(f"Inserisci valore per {col}", key=f"{col}_{idx}")
            row[col] = value
        df.loc[idx] = row
        st.write(df)
        add_another = st.selectbox(f"Aggiungi un'altra riga?", ("Si", "No"), key=f"{idx}_add_another")
        if add_another == "No":
            break
    return df

def main ():
# Titolo del form
    st.title("**Registrazione** :red[MongolCamp] :sunglasses:")
    #Bottone per scaricare csv di base

    st.subheader('Crea file csv')
    if st.button("Crea file csv"):
        df = pd.DataFrame(columns=['Nome', 'Cognome', 'Eta', 'Sesso',
                'Classe', 'Quota pagata',
                'Intolleranze','Allergie', 'Email','Foto',
                'Telefono1','Telefono2',
                'Indirizzo','Cap','Comune',
                'Giorno1','Pranzo giorno1',
                'Giorno2','Pranzo giorno2',
                'Giorno3','Pranzo giorno3',
                'Giorno4','Pranzo giorno4',
                'Ritiro bimbo','Parentela'])
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="iscrizione.csv">Download file csv</a>'
        st.markdown(href, unsafe_allow_html=True)
    # Crea un pulsante per caricare il file CSV

    st.subheader('Carica file csv')
    uploaded_file = st.file_uploader("", type="csv")

    # Se è stato caricato un file CSV, leggilo e visualizzalo in una tabella
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        df = add_rows(df)
        st.write(df)
    else:
        st.write(":red[Carica un file CSV per iniziare.]")


if __name__ == "__main__":
    main()