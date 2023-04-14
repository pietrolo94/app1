import streamlit as st
import pandas as pd

def child_camp_form():
    st.write("---")
    
    # Barra laterale per inserire il nome del bambino
    child_name = st.sidebar.text_input("Nome completo del bambino")
    
    # Barra laterale per selezionare il genere del bambino
    gender = st.sidebar.radio("Sesso", ["Maschio", "Femmina", "Altro"])
    
    # Barra laterale per inserire l'età del bambino
    age = st.sidebar.number_input("Età", min_value=5, max_value=17, step=1)
    
    # Barra laterale per selezionare eventuali allergie
    allergies = st.sidebar.multiselect("Allergie", ["Arachidi", "Latticini", "Glutine", "Altro"])
    
    # Barra laterale per selezionare le attività preferite del bambino
    activities = st.sidebar.multiselect("Attività preferite", ["Calcio", "Basket", "Pallavolo", "Arte", "Teatro", "Musica", "Altro"])
    
    # Barra laterale per inserire eventuali note
    notes = st.sidebar.text_area("Note aggiuntive", max_chars=256)
    
    st.write("# Form di registrazione per il campo estivo")
    st.write(f"## Bambino: {child_name}")
    st.write(f"### Informazioni di base")
    st.write(f"Genere: {gender}")
    st.write(f"Età: {age}")
    st.write(f"Allergie: {', '.join(allergies)}")
    st.write(f"Attività preferite: {', '.join(activities)}")
    st.write(f"Note aggiuntive: {notes}")
    
    # Creazione di un dizionario con i dati del bambino
    child_data = {
        "Nome Bambino": child_name,
        "Genere": gender,
        "Età": age,
        "Allergie": ', '.join(allergies),
        "Attività preferite": ', '.join(activities),
        "Note aggiuntive": notes
    }
    
    return child_data


def main():
    # Creazione del DataFrame vuoto
    df = pd.DataFrame(columns=["Nome Bambino", "Genere", "Età", "Allergie", "Attività preferite", "Note aggiuntive"])
    
    # Titolo dell'app
    st.title("Registrazione per campo estivo")
    
    # Creazione del modulo di registrazione
    child_data = child_camp_form()
    
    # Aggiunta dei dati del bambino al DataFrame
    df = df.append(child_data, ignore_index=True)
    
    # Bottone per salvare i dati
    if st.button("Salva dati"):
        df.to_csv("bambini_campo_estivo.csv", index=False)
        st.success("Dati salvati correttamente!")


if _name_ == "_main_":
    main()

