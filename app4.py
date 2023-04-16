import streamlit as st
import csv
import pandas as pd

#crea il file CSV se non esiste
try:
    file = open('dati_bambini.csv', 'x', newline='')
    writer = csv.writer(file)
    writer.writerow(['Nome', 'Cognome', 'Eta', 'Sesso', 'Classe', 'Quota pagata', 'Intolleranze', 'Allergie', 'Email', 'Foto', 'Telefono1', 'Telefono2', 'Indirizzo', 'Cap', 'Comune', 'Giorno1', 'Pranzo giorno1', 'Giorno2', 'Pranzo giorno2', 'Giorno3', 'Pranzo giorno3', 'Giorno4', 'Pranzo giorno4', 'Ritiro bimbo', 'Parentela','Foto'])
    file.close()
except FileExistsError:
    pass

#funzione per scrivere i dati su file
def scrivi_su_file(nome, cognome, eta, sesso, classe, quota, intolleranze, allergie, email, telefono1, telefono2, indirizzo, cap, comune, giorno1, pranzo1, giorno2, pranzo2, giorno3, pranzo3, giorno4, pranzo4, ritiro, parente, foto):
    #controlla se il bambino è già presente nel file
    with open('dati_bambini.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Nome'] == nome and row['Cognome'] == cognome:
                st.error('Bambino già registrato')
                return
    #scrive il nuovo bambino nel file
    with open('dati_bambini.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nome, cognome, eta, sesso, classe, quota, intolleranze, allergie, email, foto, telefono1, telefono2, indirizzo, cap, comune, giorno1, pranzo1, giorno2, pranzo2, giorno3, pranzo3, giorno4, pranzo4, ritiro, parente, foto])
    st.success('Dati salvati!')

#st.help(st.form)
def main():

    with st.form(key='my_form', clear_on_submit=True):
        # Titolo del form
        st.title("**Registrazione** :red[MongolCamp] :sunglasses:")
        #Anagrafica
        st.subheader('Anagrafica')
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
            eta = st.number_input("Età",min_value=3, max_value=11)
        # Campo sesso
        with col6:
            sesso = st.selectbox("Sesso", ["Maschio", "Femmina"])  
        # Campo classe
        with col7:
            classe = st.selectbox("Classe", ["Nido", "Materna","Elementari"])
        #campo quota pagata
        with col8:
            quota = st.number_input("Quota pagata", min_value=15)
        #Giorni e pranzi 
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            giorno1 = st.selectbox("Giorno 1", ["si", "no"])
            if giorno1 == "si":
                pranzo1 = st.selectbox("Pranzo Giorno1", ["si", "no"])
            else:
                pranzo1 = "no"
        with col2:
            giorno2 = st.selectbox("Giorno 2", ["si", "no"])

            pranzo2 = st.selectbox("Pranzo Giorno2", ["si", "no"])

        with col3:
            giorno3 = st.selectbox("Giorno 3", ["si", "no"])

            pranzo3 = st.selectbox("Pranzo Giorno3", ["si", "no"])

        with col4:
            giorno4 = st.selectbox("Giorno 4", ["si", "no"])

            pranzo4 = st.selectbox("Pranzo Giorno4", ["si", "no"])

        # Campo intolleranze/diete
        intolleranze = st.text_input("Intolleranze o diete")
        # Campo allergie
        allergie = st.text_input("Allergie")   
        #Recapiti
        st.subheader('Recapiti')
        col11, col12 =st.columns(2)
        with col11:
            telefono1 = st.text_input("Telefono genitore 1")
        with col12:
            telefono2 = st.text_input("Telefono genitore 2")
        # Campo email
        email = st.text_input("Email")
        #Indirizzo
        col16, col17, col18=st.columns(3)
        with col16:
            via=st.text_input("Indirizzo")
        with col17:
            cap=st.text_input("Cap")
        with col18:
            comune=st.text_input("Comune")
        #Autorizzazioni
        st.subheader('Autorizzazioni')
        col13, col14, col15=st.columns(3)
        with col13:
            ritiro = st.text_input("Persone autorizzate ritiro")
        with col14:
            parente= st.text_input("Legame Parentale")
        #autorizzazione foto
        with col15:
            foto = st.selectbox("Autorizzazione Foto", ["si", "no"])
        submit_button = st.form_submit_button(label='Salva')

    #scrive i dati su file quando si clicca sul pulsante 'Salva'
    if submit_button:
        scrivi_su_file(nome, cognome, eta, sesso, classe, quota, intolleranze, allergie, email, telefono1, telefono2, via, cap, comune, giorno1, pranzo1, giorno2, pranzo2, giorno3, pranzo3, giorno4, pranzo4, ritiro, parente, foto)
        st.success('Dati salvati!')

    #legge i dati dal file CSV e crea un dataframe pandas
    df = pd.read_csv('dati_bambini.csv')

    #visualizza i dati
    st.write('### Elenco bambini registrati')
    st.write(df)
    #crea pulsanti per scaricare il file CSV e Excel
    st.write('### Scarica dati')
    col19, col20=st.columns(2)
    with col19:
        if st.button('CSV'):
            df = pd.read_csv('dati_bambini.csv')
            csv = df.to_csv(index=False)
            st.download_button(
                label="Download CSV",
                data=csv,
                file_name='dati_bambini.csv',
                mime='text/csv'
            )
    with col20:
        if st.button('Excel'):
            df = pd.read_csv('dati_bambini.csv')
            excel = df.to_excel('dati_bambini.xlsx', index=False)
            st.download_button(
                label="Download Excel",
                data=excel,
                file_name='dati_bambini.xlsx',
                mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )

    st.write('### Rimuovi riga')
    index = st.number_input('Inserisci l\'indice della riga da rimuovere', value=0,min_value=0, max_value=len(df)-1)

    if st.button('Rimuovi'):
    #rimuove la riga selezionata dall'utente
        df.drop(index, inplace=True)
        #aggiorna il file CSV con i dati aggiornati
        df.to_csv('dati_bambini.csv', index=False)
        st.success('Riga rimossa!')
        st.write(df)
if __name__ == "__main__":
    main()