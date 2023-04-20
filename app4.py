import streamlit as st
import csv
import pandas as pd
import plotly.express as px

#crea file csv se non esiste già
try:
    file = open('dati_bambini.csv', 'x', newline='')
    writer = csv.writer(file)
    writer.writerow(['Nome', 'Cognome', 'Eta', 'Sesso', 'Classe', 'Quota pagata', 'Intolleranze', 'Allergie', 'Email', 'Foto', 'Telefono1', 'Telefono2', 'Indirizzo', 'Cap', 'Comune', 'Giorno1', 'Pranzo giorno1', 'Giorno2', 'Pranzo giorno2', 'Giorno3', 'Pranzo giorno3', 'Giorno4', 'Pranzo giorno4', 'Ritiro bimbo', 'Parentela','Foto'])
    file.close()
except FileExistsError:

    pass
try:
    file = open('educatori.csv', 'x', newline='')
    writer = csv.writer(file)
    writer.writerow(['Nome', 'Cognome', 'Ore giorno1', 'Ore giorno2', 'Ore giorno3', 'Ore giorno4', 'Ore totali', 'Compensi'])
    file.close()
except FileExistsError:

    pass
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
#funzione per scrivere i dati su file (spostata nella pagina Registrazione)
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

#funzione per scrivere i dati su file per educatori
def scrivi_su_file_ed(nome_ed, cognome_ed, ore_giorno1, ore_giorno2, ore_giorno3, ore_giorno4):
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
        writer.writerow([nome_ed, cognome_ed, ore_giorno1, ore_giorno2, ore_giorno3, ore_giorno4])
    
    st.success('Dati salvati!')
#funzione per calcolare le ore di ogni educatore
def calcola_ore_totali(df):
    df['Ore totali'] = df['Ore giorno1'] + df['Ore giorno2'] + df['Ore giorno3'] + df['Ore giorno4']
    return df
#funzione per calcolare la retribuzione di ogni educatore
def calcola_compensi(df):
    df['Compensi'] = (df['Ore giorno1'] + df['Ore giorno2'] + df['Ore giorno3'] + df['Ore giorno4'])*8
    return df
def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')
def main():
    #Setting della pagina
    st.set_page_config(page_title="Palazola", page_icon=":star:", layout="wide")
    menu = ["Inserimento Dati","Modifica Dati","Gestione educatori","Riassunto"]
    choice = st.sidebar.selectbox("Scegli una pagina", menu)
    if choice == "Inserimento Dati":
        with st.form(key='my_form', clear_on_submit=True):
            # Titolo del form
            st.title("**Registrazione** :red[Palazola Camps] :sunglasses:")
            #Anagrafica
            st.subheader('Anagrafica')
            col9, col10 = st.columns(2)
            # Campo nome
            with col9:
                nome = st.text_input("Nome")
            # Campo cognome
            with col10:
                cognome = st.text_input("Cognome")
            col5, col6, col7, col8 = st.columns(4)
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
                pranzo1 = st.selectbox("Pranzo Giorno1", ["si", "no"])
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
            col11, col12 = st.columns(2)
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
        #crea pulsanti per scaricare il file CSV 
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
        #     if st.button('Excel'):
        #         df = pd.read_csv('dati_bambini.csv')
        #         excel_path = 'dati_bambini.xlsx'
        #         df.to_excel(excel_path, index=False)
        #         st.download_button(
        #         label="Download Excel",
        #         data=excel_path,
        #         file_name='dati_bambini.xlsx',
        #         mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        #         )
        with col20:
            if st.button('Resetta elenco bambini'):
                if st.button("Sei sicuro di voler resettare l'elenco?"):
                    #resetta il dataframe a vuoto
                    df = pd.DataFrame(columns=['Nome', 'Cognome', 'Eta', 'Sesso', 'Classe', 'Quota pagata', 'Intolleranze', 'Allergie', 'Email', 'Foto', 'Telefono1', 'Telefono2', 'Indirizzo', 'Cap', 'Comune', 'Giorno1', 'Pranzo Giorno1', 'Giorno2', 'Pranzo Giorno2', 'Giorno3', 'Pranzo Giorno3', 'Giorno4', 'Pranzo Giorno4', 'Ritiro bimbo', 'Parentela','Foto'])
                    #aggiorna il file CSV con il dataframe vuoto
                    df.to_csv('dati_bambini.csv', index=False)
                    st.success('Dataframe resettato!')
                    st.write(df)

    #pagina Modifica dati
    if choice == "Modifica Dati":
        #visualizza i dati
        st.write('### Elenco bambini registrati')
        df = pd.read_csv('dati_bambini.csv')
        st.write(df)

        #sezione per modificare una cella del dataframe
        st.write('### Modifica valore')
        index_modifica = st.number_input('Inserisci l\'indice della riga da modificare', value=0, min_value=0, max_value=len(df))
        colonna_modifica = st.selectbox('Seleziona la colonna da modificare', df.columns)
        nuovo_valore = st.text_input('Inserisci il nuovo valore')
        if st.button('Modifica'):
            modifica_cella(df, index_modifica, colonna_modifica, nuovo_valore)
        
        
        #Rimuove la riga selezionata dall'utente
        st.write('### Rimuovi bambino')
        index = st.number_input('Inserisci l\'indice del bambino da rimuovere', value=0,min_value=0, max_value=len(df))

        if st.button('Rimuovi'):
        #rimuove la riga
            df.drop(index, inplace=True)
            #aggiorna il file CSV con i dati aggiornati
            df.to_csv('dati_bambini.csv', index=False)
            st.success('Bimbo rimosso!')
            st.write(df)
        #pagina Gestione educatori
    if choice == "Gestione educatori":
        #Visualizza i dati
        st.write('### Elenco educatori')
        df1 = pd.read_csv('educatori.csv')
        df1 = calcola_ore_totali(df1) # Calcola le ore totali di ogni educatore
        df1 = calcola_compensi(df1) #calcola compensi per ogni educatore
        st.write(df1)
        compensi_totali = df1['Compensi'].sum()
        st.write('Totale compensi educatori: {} euro'.format(round(compensi_totali, 2)))
        ore_totali = df1['Ore totali'].sum()
        st.write("Ore totali educatori: {}".format(round(ore_totali, 2)))
        #Dowload CSV educatori
        csv = convert_df(df1)
        st.download_button(
            "Download csv educatori",
            csv,
            "Totale_educatori.csv",
            "text/csv",
            key='download-csv'
        )
        #Form per inserire i dati degli educatori
        st.write('### Inserisci dati educatore')
        with st.form(key='educatore_form', clear_on_submit=True):
            col21, col22 = st.columns(2)
            with col21:
                nome_ed = st.text_input("Nome")
            with col22:
                cognome_ed = st.text_input("Cognome")
            col23, col24, col25, col26 = st.columns(4)
            with col23:
                ore_giorno1 = st.number_input("Ore svolte nel giorno 1", min_value=0.0, max_value=12.0, step=0.5, format="%.1f")
            with col24:
                ore_giorno2 = st.number_input("Ore svolte nel giorno 2",min_value=0.0, max_value=12.0, step=0.5, format="%.1f")
            with col25:
                ore_giorno3 = st.number_input("Ore svolte nel giorno 3",min_value=0.0, max_value=12.0, step=0.5, format="%.1f")
            with col26:
                ore_giorno4 = st.number_input("Ore svolte nel giorno 4",min_value=0.0, max_value=12.0, step=0.5, format="%.1f")
            invio = st.form_submit_button(label='Salva')
        
        #Scrivi i dati su file
        if invio:
            scrivi_su_file_ed(nome_ed,cognome_ed,ore_giorno1, ore_giorno2,ore_giorno3,ore_giorno4)

        #sezione per modificare una cella del dataframe educatori
        st.write('### Modifica valore')
        index_modifica = st.number_input('Inserisci l\'indice della riga da modificare', value=0, min_value=0, max_value=len(df1))
        colonne_ed = ['Nome', 'Cognome', 'Ore giorno1','Ore giorno2', 'Ore giorno3', 'ore giorno4']
        colonna_modifica = st.selectbox('Seleziona la colonna da modificare', colonne_ed)
        if colonna_modifica== 'Nome':
            nuovo_valore = st.text_input('Correggi nome')
        elif colonna_modifica == 'Cognome':
            nuovo_valore = st.text_input('Correggi cognome')
        else:
            nuovo_valore = st.number_input('Inserisci nuove ore')
        if st.button('Modifica'):
            modifica_cella_ed(df1, index_modifica, colonna_modifica, nuovo_valore)

        #resetta elenco educatori
        # reset = st.button('Resetta elenco educatori')
        # if reset:
        #     if st.button("Sei sicuro di voler resettare l'elenco?"):
        #         df1 = pd.DataFrame(columns=['Nome', 'Cognome', 'Ore giorno1', 'Ore giorno2', 'Ore giorno3', 'Ore giorno4','Ore totali', 'Compensi'])
        #         df1.to_csv('educatori.csv', index=False)

        #     #Visualizza il dataframe resettato
        #     st.write('### Elenco educatori')
        #     df1 = pd.read_csv('educatori.csv')
        #     st.write(df1)

    #Pagina Visualizzazione dati
    if choice == "Riassunto":
        df = pd.read_csv('dati_bambini.csv')
        df1 = pd.read_csv('educatori.csv')
        if df.empty:
            st.write(':red[Iscerisci dei dati per avere dei report]')
        else:
            st.title('Seleziona il giorno')
            giorni = ['Tutti i giorni', 'Giorno1', 'Giorno2', 'Giorno3', 'Giorno4']
            giorno = st.selectbox("Giorno", giorni)
            if giorno == 'Tutti i giorni':
                df_giorno = df
                df = df_giorno.rename(columns={'Classe': 'Numero Bambini'})
                num_bambini_per_classe = df['Numero Bambini'].value_counts()
                st.write('### Elenco Bambini')
                st.write(df_giorno[['Nome', 'Cognome', 'Eta', 'Classe', 'Telefono1', 'Telefono2']])
                fig = px.bar(num_bambini_per_classe, x=num_bambini_per_classe.index, y=num_bambini_per_classe.values, labels={'x': 'Classe', 'y':'Numero di bambini'})
                st.plotly_chart(fig, use_container_width=True)
                
                #st.write(num_bambini_per_classe)
                num_bambini_tot=df_giorno['Nome'].count()
                st.write('Numero toale bimbi: {}'.format(round(num_bambini_tot,1)))
                eta_media = df_giorno['Eta'].mean()
                st.write('Età media dei bambini registrati: {} anni'.format(round(eta_media, 1)))
                num_foto_no = (df['Foto'] == 'no').sum()
                st.write('Numero bambini no foto: {} '.format(round(num_foto_no, 1)))
                quota_media = df_giorno['Quota pagata'].mean()
                st.write('Quota media pagata dai bambini: {} euro'.format(round(quota_media, 2)))
                quota_totale = df_giorno['Quota pagata'].sum()
                st.write('Quote incassate: {} euro'.format(round(quota_totale, 2)))
                df1 = calcola_ore_totali(df1) # Calcola le ore totali di ogni educatore
                df1 = calcola_compensi(df1) #calcola compensi per ogni educatore
                compensi_totali = df1['Compensi'].sum()
                st.write('Compensi educatori: {} euro'.format(round(compensi_totali, 2)))
                ore_totali = df1['Ore totali'].sum()
                st.write("Ore totali educatori: {}".format(round(ore_totali, 2)))
                df_report = pd.DataFrame({'Numero totale bimbi':[num_bambini_tot],'Eta media bambini':[eta_media], 
                                          'Quota media':[quota_media],'Quote incassate':[quota_totale], 'Compensi educatori':[compensi_totali],
                                          'Ore totali educatori':[ore_totali]})
                csv = convert_df(df_report)
                st.download_button(
                "Download report totale csv",
                csv,
                "Report_totale.csv",
                "text/csv",
                key='download-csv'
                )
            else:
                #filtra il DataFrame per il giorno selezionato
                df_giorno = df.loc[df['{}' .format(giorno)] == 'si']
        
                df_giorno = df_giorno[['Nome','Cognome', 'Eta', 'Classe', 'Pranzo Giorno{}'.format(giorno[-1]),'Foto', 'Intolleranze', 'Allergie']]
                #visualizza i dati
                st.write('### Elenco bambini{}:'.format('' if giorno=='Tutti i giorni' else '  {}'.format(giorno)))
                df_giorno = df_giorno.assign(Colonna1='', Colonna2='')
                st.write(df_giorno)
                df_giorno = df_giorno.rename(columns={'Classe': 'Numero Bambini'})
                num_bambini_per_classe =df_giorno['Numero Bambini'].value_counts()
                # fig = px.bar(num_bambini_per_classe, x=num_bambini_per_classe.index, y=num_bambini_per_classe.values, labels={'x': 'Classe', 'y':'Numero di bambini'})
                # st.plotly_chart(fig, use_container_width=True)
                st.write(num_bambini_per_classe)
                pranzi=df_giorno['Pranzo Giorno{}'.format(giorno[-1])].value_counts()
                st.write(pranzi)
                foto_no = df_giorno.loc[df_giorno['Foto'] == 'no']
                if not foto_no.empty:
                    st.write('### Bambini senza autorizzazione foto:')
                    st.write(foto_no[['Nome', 'Cognome']])
if __name__ == "__main__":
    main()