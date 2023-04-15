import streamlit as st
import pandas as pd
import os

def add_row_to_csv(csv_path, df):
    # Leggi il file csv esistente come un dataframe
    existing_df = pd.read_csv(csv_path)
    
    # Aggiungi il nuovo dataframe come riga al dataframe esistente
    updated_df = pd.concat([existing_df, df], ignore_index=True)
    
    # Scrivi il dataframe aggiornato sul file csv
    updated_df.to_csv(csv_path, index=False)    

def main():
    
    # Titolo del form
    st.title("**Registrazione** :red[MongolCamp] :sunglasses:")

    col9, col10 = st.columns(2)
    # Campo nome
    with col9:
        nome = st.text_input("Nome")
    # Campo cognome
    with col10:
        cognome = st.text_input("Cognome")

    col5, col6, col7, col8 =st.columns(4)
    # Campo età
    with col5:
        age = st.number_input("Età",min_value=3, max_value=11)
    # Campo sesso
    with col6:
        sesso = st.selectbox("Sesso", ["Maschio", "Femmina"])  
    # Campo classe
    with col7:
        classe = st.selectbox("Classe", ["Nido", "Materna","Elementari"])
    #campo quota pagata
    with col8:
        quota = st.number_input("Quota pagata", min_value=15)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        giorno1 = st.selectbox("Giorno 1", ["si", "no"])
        if giorno1 == "si":
            pranzo1 = st.selectbox("Pranzo Giorno1", ["si", "no"])
        else:
            pranzo1 = "no"
    with col2:
        giorno2 = st.selectbox("Giorno 2", ["si", "no"])
        if giorno2 == "si":
            pranzo2 = st.selectbox("Pranzo Giorno2", ["si", "no"])
        else:
            pranzo2 = "no"
    with col3:
        giorno3 = st.selectbox("Giorno 3", ["si", "no"])
        if giorno3 == "si":
            pranzo3 = st.selectbox("Pranzo Giorno3", ["si", "no"])
        else:
            pranzo3 = "no"
    with col4:
        giorno4 = st.selectbox("Giorno 4", ["si", "no"])
        if giorno4 == "si":
            pranzo4 = st.selectbox("Pranzo Giorno4", ["si", "no"])
        else:
            pranzo4 = "no"
    # Campo intolleranze/diete
    intolleranze = st.text_input("Intolleranze o diete")

    # Campo allergie
    allergie = st.text_input("Allergie")

    # Campo telefono di emergenza
    col11, col12 =st.columns(2)
    with col11:
        telefono1 = st.text_input("Telefono genitore 1")

    with col12:
        telefono2 = st.text_input("Telefono genitore 2")

    # Campo email
    email = st.text_input("Email")
    
    #Autorizzazione foto
    foto = st.selectbox("Autorizzazione Foto", ["si", "no"])

    #campo giorni
    # Creiamo 4 colonne utilizzando st.beta_columns()
    
    #Ritiro bimbi
    st.subheader('Autorizzazione ritiro')
    col13, col14=st.columns(2)
    with col13:
        ritiro = st.text_input("Nome e cognome persone autorizzate")
    with col14:
        parente= st.text_input("Legame Parentale")
    # NOME DEL FILE CSV
    FILENAME = 'registrazione.csv'

    # VERIFICA SE IL FILE ESISTE
    if not os.path.exists(FILENAME):
        # CREA UN DATAFRAME VUOTO
        df = pd.DataFrame(columns=['Nome', 'Cognome', 'Età', 'Sesso',
                'Classe', 'Quota pagata',
                'Allergie', 'Email', 'Telefono1',
                'Giorno1','Pranzo giorno1',
                'Giorno2','Pranzo giorno2',
                'Giorno3','Pranzo giorno3',
                'Giorno4','Pranzo giorno4',
                'Ritiro bimbo','Parentela'])
    # SALVA IL DATAFRAME IN UN FILE CSV
        df.to_csv(FILENAME, index=False)

    # CARICA I DATI DAL FILE CSV
    df = pd.read_csv(FILENAME)

    # aggiungere un pulsante per salvare i dati in un file CSV
    if st.button("Salva dati"):
        # creare un dataframe con i dati inseriti
        data = {'Nome': [nome], 'Cognome':[cognome], 'Età':[age], 'Sesso':[sesso],
                'Classe':[classe], 'Quota pagata':[quota],
                'Allergie':[allergie], 'Email': [email], 'Telefono1': [telefono1],
                'Giorno1':giorno1,'Pranzo giorno1':[pranzo1],
                'Giorno2':giorno2,'Pranzo giorno2':[pranzo2],
                'Giorno3':giorno3,'Pranzo giorno3':[pranzo3],
                'Giorno4':giorno4,'Pranzo giorno4':[pranzo4],
                'Ritiro bimbo':[ritiro],'Parentela':[parente]
                }
        df = pd.DataFrame(data)
        # salvare il dataframe in un file CSV
        add_row_to_csv("registrazione.csv", df)
        # mostrare un messaggio di conferma
        st.success("Dati registrati con successo nel file CSV!")

if __name__ == "__main__":
    main()