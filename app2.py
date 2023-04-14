import streamlit as st
import pandas as pd

# Funzione per creare un nuovo modulo
def create_form():
    name = st.text_input("Nome")
    age = st.number_input("Età")
    gender = st.selectbox("Genere", ['Maschio', 'Femmina'])
    guardian_name = st.text_input("Nome del tutore legale")
    emergency_contact = st.text_input("Contatto di emergenza")
    medical_info = st.text_area("Informazioni mediche")

    # Aggiungiamo i dati ad un DataFrame
    data = {
        'Nome': [name],
        'Età': [age],
        'Genere': [gender],
        'Tutore legale': [guardian_name],
        'Contatto di emergenza': [emergency_contact],
        'Informazioni mediche': [medical_info]
    }
    df = pd.DataFrame(data)

    # Aggiungiamo i dati al file CSV
    with open('bambini.csv', 'a') as f:
        df.to_csv(f, header=f.tell()==0, index=False)

    st.success("Modulo compilato con successo!")    

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

# Creiamo l'interfaccia utente
def main():
    st.title("Form di iscrizione al campo estivo")

# Bottone per creare un nuovo modulo
    if st.button("Nuovo modulo"):
        create_form()

    add_bg_from_url()
if __name__ == "__main__":
    main()