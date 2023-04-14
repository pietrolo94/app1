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

def child_camp_form():
    st.write("---")
    
    # Barra laterale per inserire il nome del bambino
    child_name = st.sidebar.text_input("Nome completo del bambino")
    
    # Barra laterale per selezionare il genere del bambino
    gender = st.sidebar.radio("Sesso", ["Maschio", "Femmina", "Altro"])
    
    # Barra laterale per inserire l'età del bambino
    age = st.sidebar.number_input("Età", min_value=3, max_value=11, step=1)
    
    # Barra laterale per selezionare eventuali allergie
    allergies = st.sidebar.multiselect("Allergie", ["Arachidi", "Latticini", "Glutine", "Altro"])
    
    # Barra laterale per selezionare le attività preferite del bambino
    school = st.sidebar.multiselect("Scuola frequentata", ["Nido", "Materna", "Elementari", "Niente", "Altro"])
    
    # Barra laterale per inserire mail
    email = st.sidebar.text_area("Email", max_chars=50)

    #Barra laterale per inserire numero emergenza
    telephone = st.sidebar.text_input("Numero di emergenza",max_chars=10 )

    notes = st.sidebar.text_area("Note aggiuntive", max_chars=256)

    st.write(f"## Nome bimbo: {child_name}")
    st.write(f"### Informazioni di base")
    st.write(f"Genere: {gender}")
    st.write(f"Età: {age}")
    st.write(f"Allergie: {', '.join(allergies)}")
    st.write(f"Scuola: {', '.join(school)}")
    st.write(f"Email: {email}")
    st.write(f"Numero di emergenza: {telephone}")
    st.write(f"Note aggiuntive: {notes}")
    
    # Creazione di un dizionario con i dati del bambino
    child_data = {
        "Nome Bambino": child_name,
        "Genere": gender,
        "Età": age,
        "Allergie": ', '.join(allergies),
        "Attività preferite": ', '.join(school),
        "Email": ','.join(email),
        "Numero di emergenza": ','.join(telephone),
        "Note aggiuntive": notes
    }
    
    return child_data


def main():
    # Creazione del DataFrame vuoto
    df = pd.DataFrame(columns=["Nome Bambino", "Genere", "Età", "Allergie", "Attività preferite", "Note aggiuntive"])
    
    # Titolo dell'app
    st.title("Registrazione bimbi Palaminchia")
    
    # Creazione del modulo di registrazione
    child_data = child_camp_form()
    
    # Aggiunta dei dati del bambino al DataFrame
    df = df.append(child_data, ignore_index=True)
    
    # Bottone per salvare i dati
    if st.button("Salva dati"):
        df.to_csv("bambini_campo_estivo.csv", index=False)
        st.success("Dati salvati correttamente!")

    add_bg_from_url()

if __name__ == "__main__":
    main()