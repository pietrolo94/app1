import streamlit as st
import csv
import pandas as pd

#funzione modifica cella bambini
def modifica_cella(df, index, colonna, valore):
    df.at[index, colonna] = valore
    df.to_csv('dati_bambini.csv', index=False)
    st.success('Valore modificato!')
    st.write(df)
#funzione modifica cella educatori
def modifica_cella_ed(df, index, colonna, valore):
    df.at[index, colonna] = valore
    df.to_csv('educatori.csv', index=False)
    st.success('Valore modificato!')
# Funzione per modificare un valore nella tabella delle spese
def modify_expense_data(row_index, new_value):
    df = pd.read_csv('spese.csv')
    df.at[row_index, 'Importo'] = new_value
    df.to_csv('spese.csv', index=False)
# Funzione per rimuovere una riga dalla tabella delle spese
def remove_expense_data(row_index):
    df = pd.read_csv('spese.csv')
    df.drop(row_index, inplace=True)
    df.to_csv('spese.csv', index=False)
#funzione per scrivere i dati su file (spostata nella pagina Registrazione)
def scrivi_su_file(nome, cognome, eta, sesso, classe, quota, diete, allergie, email, telefono1, telefono2, indirizzo, cap, comune, giorno1, pranzo1, giorno2, pranzo2, giorno3, pranzo3, giorno4, pranzo4, giorno5, pranzo5, giorno6, pranzo6, giorno7, pranzo7, giorno8, pranzo8, tesseramento, ritiro, parente, foto):
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
        writer.writerow([nome, cognome, eta, sesso, classe, quota, diete, allergie, email, telefono1, telefono2, indirizzo, cap, comune, giorno1, pranzo1, giorno2, pranzo2, giorno3, pranzo3, giorno4, pranzo4, giorno5, pranzo5, giorno6, pranzo6, giorno7, pranzo7, giorno8, pranzo8, tesseramento, ritiro, parente, foto])

#funzione per scrivere i dati su file per educatori
def scrivi_su_file_ed(nome_ed, cognome_ed, ore_giorno1, ore_giorno2, ore_giorno3, ore_giorno4, ore_giorno5, ore_giorno6, ore_giorno7, ore_giorno8):
    #controlla se l'educatore è già presente nel file
    with open('educatori.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Nome'] == nome_ed and row['Cognome'] == cognome_ed:
                st.error('Educatore già registrato')
                return
    
    #scrive il nuovo educatore nel file
    with open('educatori.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nome_ed, cognome_ed, ore_giorno1, ore_giorno2, ore_giorno3, ore_giorno4, ore_giorno5, ore_giorno6, ore_giorno7, ore_giorno8])
    
    st.success('Dati salvati!')
#funzione per scrivere su file spese
def save_expense_data(tipo_spesa, importo):
    with open("spese.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([tipo_spesa, importo])
    st.success("Spesa aggiunta con successo!")
#funzione per calcolare le ore di ogni educatore
def calcola_ore_totali(df):
    df['Ore totali'] = df['Ore giorno1'] + df['Ore giorno2'] + df['Ore giorno3'] + df['Ore giorno4'] + df['Ore giorno5'] + df['Ore giorno6'] + df['Ore giorno7'] + df['Ore giorno8']
    return df
#funzione per calcolare la retribuzione di ogni educatore
def calcola_compensi(df):
    df['Compensi'] = (df['Ore giorno1'] + df['Ore giorno2'] + df['Ore giorno3'] + df['Ore giorno4']+ df['Ore giorno5'] + df['Ore giorno6'] + df['Ore giorno7'] + df['Ore giorno8'])*9
    return df
def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')