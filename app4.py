import streamlit as st
import csv
import pandas as pd
from funzioni import *
import io
import xlsxwriter

#crea file csv se non esiste già
try:
    file = open('dati_bambini.csv', 'x', newline='')
    writer = csv.writer(file)
    writer.writerow(['Nome', 'Cognome', 'Eta', 'Sesso', 'Classe', 'Quota pagata', 'Diete', 'Allergie', 'Email', 'Telefono1', 'Telefono2', 'Indirizzo', 'Cap', 'Comune', 'Giorno1', 'Pranzo giorno1', 'Giorno2', 'Pranzo giorno2', 'Giorno3', 'Pranzo giorno3', 'Giorno4', 'Pranzo giorno4', 'Giorno5', 'Pranzo giorno5', 'Giorno6', 'Pranzo giorno6', 'Giorno7', 'Pranzo giorno7', 'Giorno8', 'Pranzo giorno8', 'Tesseramento', 'Ritiro bimbo', 'Parentela','Foto'])
    file.close()
except FileExistsError:

    pass
try:
    file = open('educatori.csv', 'x', newline='')
    writer = csv.writer(file)
    writer.writerow(['Nome', 'Cognome', 'Ore giorno1', 'Ore giorno2', 'Ore giorno3', 'Ore giorno4','Ore giorno5', 'Ore giorno6', 'Ore giorno7', 'Ore giorno8', 'Ore totali', 'Compensi'])
    file.close()
except FileExistsError:

    pass
try:
    file = open('spese.csv', 'x', newline='')
    writer = csv.writer(file)
    writer.writerow(['Tipo','Importo'])
    file.close()
except FileExistsError:

    pass

def main():
    #Setting della pagina
    st.set_page_config(page_title="Palazola", page_icon=":star:", layout="wide")
    # Menu
    menu = ["Inserimento Dati","Modifica Dati","Gestione educatori","Spese","Riassunto"]

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
                eta = st.number_input("Età", value=6, min_value=3, max_value=14)
            # Campo sesso
            with col6:
                sesso = st.selectbox("Sesso", ["Maschio", "Femmina"])
            # Campo classe
            with col7:
                classe = st.selectbox("Classe", ["Elementari","Materna","Medie","Nido"])
            #campo quota pagata
            with col8:
                quota = st.number_input("Quota pagata",value=135, min_value=0,max_value=500)
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

            col27, col28, col29, col30 = st.columns(4)
            with col27:
                giorno5 = st.selectbox("Giorno 5", ["si", "no"])
                pranzo5 = st.selectbox("Pranzo Giorno5", ["si", "no"])
            with col28:
                giorno6 = st.selectbox("Giorno 6", ["si", "no"])
                pranzo6 = st.selectbox("Pranzo Giorno6", ["si", "no"])
            with col29:
                giorno7 = st.selectbox("Giorno 7", ["si", "no"])
                pranzo7 = st.selectbox("Pranzo Giorno7", ["si", "no"])
            with col30:
                giorno8 = st.selectbox("Giorno 8", ["si", "no"])
                pranzo8 = st.selectbox("Pranzo Giorno8", ["si", "no"])
            
            #tesseramento
            tesseramento = st.number_input("Costo tesseramento",value=3)

            # Campo intolleranze/diete
            diete = st.text_input("Diete")
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
            scrivi_su_file(nome, cognome, eta, sesso, classe, quota, diete, allergie, email, telefono1, telefono2, via, cap, comune, giorno1, pranzo1, giorno2, pranzo2, giorno3, pranzo3, giorno4, pranzo4, giorno5, pranzo5, giorno6, pranzo6, giorno7, pranzo7, giorno8, pranzo8, tesseramento, ritiro, parente, foto)
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
            if st.button('Scarica elenco bambini'):
                excel_file = 'Palazola_.xlsx'
                output = io.BytesIO()
                writer = pd.ExcelWriter(output, engine='xlsxwriter')
                df.to_excel(writer,sheet_name='Elenco_tot', index=False)
                writer.save()
                writer.close()  # chiude l'oggetto writer
                output.seek(0)
                st.download_button(
                    label="Download Xlsx",
                    data=output,
                    file_name=excel_file,
                    mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
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
                #resetta il dataframe a vuoto
                df = pd.DataFrame(columns=['Nome', 'Cognome', 'Eta', 'Sesso', 'Classe', 'Quota pagata', 'Diete', 'Allergie', 'Email', 'Telefono1', 'Telefono2', 'Indirizzo', 'Cap', 'Comune', 'Giorno1', 'Pranzo giorno1', 'Giorno2', 'Pranzo giorno2', 'Giorno3', 'Pranzo giorno3', 'Giorno4', 'Pranzo giorno4','Giorno5', 'Pranzo giorno5', 'Giorno6', 'Pranzo giorno6', 'Giorno7', 'Pranzo giorno7', 'Giorno8', 'Pranzo giorno8', 'Tesseramento', 'Ritiro bimbo', 'Parentela', 'Foto'])
                #aggiorna il file CSV con il dataframe vuoto
                df.to_csv('dati_bambini.csv', index=False)
                st.success('Dataframe resettato!')

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
    #pagina gestione educatori
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
        if st.button('Scarica report educatori', key=1):
            excel_file = 'Report_educatori.xlsx'
            output = io.BytesIO()
            writer = pd.ExcelWriter(output, engine='xlsxwriter')
            df1.to_excel(writer,sheet_name='Report_educatori', index=False)
            writer.save()
            output.seek(0)
            st.download_button(
                label="Download Xlsx",
                data=output,
                file_name=excel_file,
                mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
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
                ore_giorno5 = st.number_input("Ore svolte nel giorno 5", min_value=0.0, max_value=12.0, step=0.5, format="%.1f")
            with col24:
                ore_giorno2 = st.number_input("Ore svolte nel giorno 2",min_value=0.0, max_value=12.0, step=0.5, format="%.1f")
                ore_giorno6 = st.number_input("Ore svolte nel giorno 6", min_value=0.0, max_value=12.0, step=0.5, format="%.1f")
            with col25:
                ore_giorno3 = st.number_input("Ore svolte nel giorno 3",min_value=0.0, max_value=12.0, step=0.5, format="%.1f")
                ore_giorno7 = st.number_input("Ore svolte nel giorno 7", min_value=0.0, max_value=12.0, step=0.5, format="%.1f")
            with col26:
                ore_giorno4 = st.number_input("Ore svolte nel giorno 4",min_value=0.0, max_value=12.0, step=0.5, format="%.1f")
                ore_giorno8 = st.number_input("Ore svolte nel giorno 8", min_value=0.0, max_value=12.0, step=0.5, format="%.1f")
            invio = st.form_submit_button(label='Salva')
        
        #Scrivi i dati su file
        if invio:
            scrivi_su_file_ed(nome_ed,cognome_ed,ore_giorno1, ore_giorno2,ore_giorno3,ore_giorno4, ore_giorno5, ore_giorno6,ore_giorno7,ore_giorno8)
        #sezione per modificare una cella del dataframe educatori
        st.write('### Modifica valore')
        index_modifica = st.number_input('Inserisci l\'indice della riga da modificare', value=0, min_value=0, max_value=len(df1))
        colonne_ed = ['Nome', 'Cognome', 'Ore giorno1','Ore giorno2', 'Ore giorno3', 'ore giorno4','Ore giorno5', 'Ore giorno6', 'Ore giorno7', 'Ore giorno8',]
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
        reset = st.button('Resetta elenco educatori')
        if reset:
            df1 = pd.DataFrame(columns=['Nome', 'Cognome', 'Ore giorno1', 'Ore giorno2', 'Ore giorno3', 'Ore giorno4','Ore giorno5', 'Ore giorno6', 'Ore giorno7','Ore giorno8', 'Ore totali', 'Compensi'])
            df1.to_csv('educatori.csv', index=False)
            st.success('Elenco resettato')
        #     #Visualizza il dataframe resettato
        #     st.write('### Elenco educatori')
        #     df1 = pd.read_csv('educatori.csv')
        #     st.write(df1)
    #pagina gestione spese
    if choice == "Spese":
        st.title("Registrazione delle spese")
        st.write("### Elenco spese")
        df = pd.read_csv('spese.csv')
        st.write(df)
        if st.button('Scarica lista spese'):
            excel_file = 'Spese.xlsx'
            output = io.BytesIO()
            writer = pd.ExcelWriter(output, engine='xlsxwriter')
            df.to_excel(writer,sheet_name='Spese', index=False)
            writer.save()
            output.seek(0)
            st.download_button(
                label="Download Xlsx",
                data=output,
                file_name=excel_file,
                mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )

        with st.form(key="spese_form", clear_on_submit=True):
            tipo_spesa = st.text_input("Tipo di spesa", key="tipo_spesa")
            importo = st.number_input("Importo", key="importo")
            submit_button = st.form_submit_button(label="Aggiungi spesa")

        # Salvataggio dati su file CSV
        if submit_button:
            save_expense_data(tipo_spesa, importo)
        # Aggiunta bottoni "Modifica valore" e "Rimuovi riga" alla tabella
        st.write('#### Modifica valori')
        idx = st.number_input('indice spesa da modificare', value=0,min_value=0, max_value=len(df))
        costo = st.number_input('nuovo importo',value=0.0)
        if st.button("modifica"):
            modify_expense_data(idx, costo)
            st.write(df)
        st.write('#### rimuovi spesa')
        idx2 = st.number_input('indice spesa da rimuovere', value=0,min_value=0, max_value=len(df))
        if st.button('rimuovi'):
            remove_expense_data(idx2)
    #Pagina Visualizzazione dati
    if choice == "Riassunto":
        df = pd.read_csv('dati_bambini.csv')
        if df.empty:
            st.write(':red[Iscerisci dei dati per avere dei report]')
        else:
            st.title('Seleziona il giorno')
            giorni = ['Tutti i giorni', 'Giorno1', 'Giorno2', 'Giorno3', 'Giorno4', 'Giorno5', 'Giorno6', 'Giorno7', 'Giorno8']
            giorno = st.selectbox("Giorno", giorni)
            if giorno == 'Tutti i giorni':
                df = pd.read_csv('dati_bambini.csv')
                df1 = pd.read_csv('educatori.csv')
                df2 = pd.read_csv('spese.csv')
                df_giorno = df
                df = df_giorno.rename(columns={'Classe': 'Numero Bambini'})
                num_bambini_per_classe = df['Numero Bambini'].value_counts()
                st.write('### Elenco Bambini')
                st.write(df_giorno[['Nome', 'Cognome', 'Eta', 'Classe', 'Telefono1', 'Telefono2']])
                #fig = px.bar(num_bambini_per_classe, x=num_bambini_per_classe.index, y=num_bambini_per_classe.values, labels={'x': 'Classe', 'y':'Numero di bambini'})
                #st.plotly_chart(fig, use_container_width=True)
                
                #st.write(num_bambini_per_classe)
                num_bambini_tot=df_giorno['Nome'].count()
                st.write('Numero toale bimbi: {}'.format(round(num_bambini_tot,1)))
                eta_media = df_giorno['Eta'].mean()
                st.write('Età media dei bambini registrati: {} anni'.format(round(eta_media, 2)))
                quota_media = df_giorno['Quota pagata'].mean()
                st.write('Quota media pagata dai bambini: {} euro'.format(round(quota_media, 2)))
                quota_totale = df_giorno['Quota pagata'].sum()
                st.write('Incasso lordo: {} euro'.format(round(quota_totale, 2)))
                costo_tesseramenti = df['Tesseramento'].sum()
                st.write('Costo tesseramento: {} euro'.format(round(costo_tesseramenti, 2)))
                df1 = calcola_ore_totali(df1) # Calcola le ore totali di ogni educatore
                df1 = calcola_compensi(df1) #calcola compensi per ogni educatore
                compensi_totali = df1['Compensi'].sum()
                st.write('Compensi educatori: {} euro'.format(round(compensi_totali, 2)))
                ore_totali = df1['Ore totali'].sum()
                st.write("Ore totali educatori: {}".format(round(ore_totali, 2)))
                spese = df2['Importo'].sum()
                costo_pranzi = (count_value(df,'Pranzo giorno1','si')+count_value(df,'Pranzo giorno2','si')+count_value(df,'Pranzo giorno3','si')+count_value(df,'Pranzo giorno4','si')+count_value(df,'Pranzo giorno5','si')+count_value(df,'Pranzo giorno6','si')+count_value(df,'Pranzo giorno7','si')+count_value(df,'Pranzo giorno8','si'))*7.5
                st.write('Costo totale pranzi: {} euro'.format(round(costo_pranzi, 2)))
                st.write('Totale spese:{} euro'.format(round(spese, 2)))
                incasso_netto = quota_totale-compensi_totali-spese-costo_tesseramenti-costo_pranzi
                st.write('Incasso netto: {} euro'.format(round(incasso_netto, 2)))
                df_report = pd.DataFrame({'Numero totale bambini':[num_bambini_tot],'Eta media':[eta_media], 
                                          'Quota media':[quota_media],'Incasso lordo':[quota_totale], 'Compensi educatori':[compensi_totali],
                                          'Ore totali educatori':[ore_totali],'Totale spese':[spese],'Costo tesseramento bimbi':[costo_tesseramenti],'Costo pranzi':[costo_pranzi],'Incasso netto':[incasso_netto]})
                st.write(df_report)
                #Download report finale
                if st.button('Scarica report finale'):
                    excel_file = 'Report_finale.xlsx'
                    output = io.BytesIO()
                    writer = pd.ExcelWriter(output, engine='xlsxwriter')
                    df_report.to_excel(writer,sheet_name='Report_finale', index=False)
                    writer.save()
                    output.seek(0)
                    st.download_button(
                        label="Download Xlsx",
                        data=output,
                        file_name=excel_file,
                        mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                    )
            else:
                #filtra il DataFrame per il giorno selezionato
                df_giorno = df.loc[df['{}' .format(giorno)] == 'si']
        
                df_giorno = df_giorno[['Nome','Cognome', 'Eta', 'Classe', 'Pranzo giorno{}'.format(giorno[-1]),'Foto', 'Diete', 'Allergie']]
                df_giorno_nido_materna = df_giorno.loc[df_giorno['Classe'].isin(['Nido', 'Materna'])]
                df_giorno_elementari_medie = df_giorno.loc[df_giorno['Classe'].isin(['Elementari', 'Medie'])]
                #visualizza i dati
                st.write('### Elenco bambini{}:'.format('' if giorno=='Tutti i giorni' else '  {}'.format(giorno)))
                st.write('#### Elenco bimbi materna-nido')
                df_giorno_nido_materna = df_giorno_nido_materna.assign(Primo='', Secondo='')
                st.write(df_giorno_nido_materna)
                st.write('#### Elenco bimbi elementari-medie')
                df_giorno_elementari_medie = df_giorno_elementari_medie.assign(Primo='', Secondo='')
                st.write(df_giorno_elementari_medie)
                col31, col32 = st.columns(2)
                with col31:
                    if st.button('Scarica elenco materna-nido', key=1):
                        excel_file = 'Materna-nido_giorno{}.xlsx'.format(giorno[-1])
                        output = io.BytesIO()
                        writer = pd.ExcelWriter(output, engine='xlsxwriter')
                        df_giorno_nido_materna.to_excel(writer,sheet_name='Materna-nido_giorno{}'.format(giorno[-1]), index=False)
                        writer.save()
                        output.seek(0)
                        st.download_button(
                            label="Download Xlsx",
                            data=output,
                            file_name=excel_file,
                            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                        )
                with col32:    
                    if st.button('Scarica elenco elementari_medie', key=2):
                        excel_file = 'Emelentari_medie_giorno{}.xlsx'.format(giorno[-1])
                        output = io.BytesIO()
                        writer = pd.ExcelWriter(output, engine='xlsxwriter')
                        df_giorno_elementari_medie.to_excel(writer,'Emelentari_medie_giorno{}'.format(giorno[-1]), index=False)
                        writer.save()
                        output.seek(0)
                        st.download_button(
                            label="Download Xlsx",
                            data=output,
                            file_name=excel_file,
                            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                        )
                df_giorno = df_giorno.rename(columns={'Classe': 'Numero Bambini'})
                num_bambini_per_classe =df_giorno['Numero Bambini'].value_counts()
                # fig = px.bar(num_bambini_per_classe, x=num_bambini_per_classe.index, y=num_bambini_per_classe.values, labels={'x': 'Classe', 'y':'Numero di bambini'})
                # st.plotly_chart(fig, use_container_width=True)
                st.write(num_bambini_per_classe)
                pranzi=df_giorno['Pranzo giorno{}'.format(giorno[-1])].value_counts()
                st.write(pranzi)
                foto_no = df_giorno.loc[df_giorno['Foto'] == 'no']
                if not foto_no.empty:
                    st.write('### Bambini senza autorizzazione foto:')
                    st.write(foto_no[['Nome', 'Cognome']])
if __name__ == "__main__":
    main()