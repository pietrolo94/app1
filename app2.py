import streamlit as st
import pandas as pd

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2019/04/24/11/27/flowers-4151900_960_720.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
def add_row_to_csv(csv_path, df):
    # Leggi il file csv esistente come un dataframe
    existing_df = pd.read_csv(csv_path)
    
    # Aggiungi il nuovo dataframe come riga al dataframe esistente
    updated_df = existing_df.append(df, ignore_index=True)
    
    # Scrivi il dataframe aggiornato sul file csv
    updated_df.to_csv(csv_path, index=False)    

def main():
    
    # Titolo del form
    st.title("Registrazione")

    # Campo nome
    nome = st.text_input("Nome")

    # Campo cognome
    cognome = st.text_input("Cognome")

    age = st.number_input("Età",min_value=3, max_value=11)

    # Campo sesso
    sesso = st.selectbox("Sesso", ["Maschio", "Femmina"])  

    # Campo allergie
    allergie = st.text_input("Allergie")

    # Campo telefono di emergenza
    telefono = st.text_input("Telefono di emergenza")

    # Campo email
    email = st.text_input("Email")

    #campo giorni

    # Creiamo due colonne utilizzando st.beta_columns()
    col1, col2, col3, col4 = st.columns(4)

    # Inseriamo le selectbox nelle colonne
    with col1:
        giorno1 = st.selectbox("Giorno 1", ["si", "no"])

    with col2:
        giorno2 = st.selectbox("Giorno 2", ["si", "no"])
    
    with col3:
        giorno3 = st.selectbox("Giorno 3", ["si", "no"])
        
    with col3:
        giorno4 = st.selectbox("Giorno 4", ["si", "no"])

    # aggiungere un pulsante per salvare i dati in un file CSV
    if st.button("Salva dati"):
        # creare un dataframe con i dati inseriti
        data = {'Nome': [nome], 'Cognome':[cognome], 'Età':[age], 'Sesso':[sesso],
                'Allergie':[allergie], 'Email': [email], 'Telefono': [telefono],
                'Giorno1':giorno1, 'Giorno2':giorno2,'Giorno3':giorno3, 'Giorno4':giorno4
                }
        df = pd.DataFrame(data)
        # salvare il dataframe in un file CSV
        add_row_to_csv("registrazione.csv", df)
        # mostrare un messaggio di conferma
        st.success("Dati registrati con successo nel file CSV!")
    add_bg_from_url()
    
if __name__ == "__main__":
    main()