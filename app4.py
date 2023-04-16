import streamlit as st
import csv

#crea il file CSV se non esiste
try:
    file = open('dati_bambini.csv', 'x', newline='')
    writer = csv.writer(file)
    writer.writerow(['Nome', 'Cognome', 'Eta', 'Sesso', 'Classe', 'Quota pagata', 'Intolleranze', 'Allergie', 'Email', 'Foto', 'Telefono1', 'Telefono2', 'Indirizzo', 'Cap', 'Comune', 'Giorno1', 'Pranzo giorno1', 'Giorno2', 'Pranzo giorno2', 'Giorno3', 'Pranzo giorno3', 'Giorno4', 'Pranzo giorno4', 'Ritiro bimbo', 'Parentela'])
    file.close()
except FileExistsError:
    pass

#funzione per scrivere i dati su file
def scrivi_su_file(nome, cognome, eta, sesso, classe, quota_pagata, intolleranze, allergie, email, foto, telefono1, telefono2, indirizzo, cap, comune, giorno1, pranzo_giorno1, giorno2, pranzo_giorno2, giorno3, pranzo_giorno3, giorno4, pranzo_giorno4, ritiro_bimbo, parentela):
    file = open('dati_bambini.csv', 'a', newline='')
    writer = csv.writer(file)
    writer.writerow([nome, cognome, eta, sesso, classe, quota_pagata, intolleranze, allergie, email, foto, telefono1, telefono2, indirizzo, cap, comune, giorno1, pranzo_giorno1, giorno2, pranzo_giorno2, giorno3, pranzo_giorno3, giorno4, pranzo_giorno4, ritiro_bimbo, parentela])
    file.close()

#form per la raccolta dei dati
st.write('# Inserisci i dati del bambino')
with st.form(key='my_form'):
    nome = st.text_input('Nome')
    cognome = st.text_input('Cognome')
    eta = st.number_input('Età', min_value=0)
    sesso = st.radio('Sesso', ['Maschio', 'Femmina'])
    classe = st.text_input('Classe')
    quota_pagata = st.number_input('Quota pagata', min_value=0)
    intolleranze = st.text_input('Intolleranze')
    allergie = st.text_input('Allergie')
    email = st.text_input('Email')
    foto = st.text_input('Foto')
    telefono1 = st.text_input('Telefono1')
    telefono2 = st.text_input('Telefono2')
    indirizzo = st.text_input('Indirizzo')
    cap = st.text_input('CAP')
    comune = st.text_input('Comune')
    giorno1 = st.text_input('Giorno1')
    pranzo_giorno1 = st.text_input('Pranzo giorno1')
    giorno2 = st.text_input('Giorno2')
    pranzo_giorno2 = st.text_input('Pranzo giorno2')
    giorno3 = st.text_input('Giorno3')
    pranzo_giorno3 = st.text_input('Pranzo giorno3')
    giorno4 = st.text_input('Giorno4')
    pranzo_giorno4 = st.text_input('Pranzo giorno4')
    ritiro_bimbo = st.text_input('Ritiro bimbo')
    parentela = st.text_input('Parentela')
    submit_button = st.form_submit_button(label='Salva')

#scrive i dati su file quando si clicca sul pulsante 'Salva'
if submit_button:
    scrivi_su_file(nome, cognome, eta, sesso, classe, quota_pagata, intolleranze, allergie, email, foto, telefono1, telefono2, indirizzo, cap, comune, giorno1, pranzo_giorno1, giorno2, pranzo_giorno2, giorno3, pranzo_giorno3, giorno4, pranzo_giorno4, ritiro_bimbo, parentela)
    st.success('Dati salvati!')

#pulsante per ricaricare la pagina
if st.button('Aggiorna'):
    st.experimental_rerun()