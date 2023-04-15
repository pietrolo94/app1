import base64
import streamlit as st
import pandas as pd


def aggiungi_riga(df,nome,cognome,age,sesso,classe,quota,intolleranze,allergie,email,foto,
                  telefono1,telefono2,via,cap,comune,giorno1,pranzo1,giorno2,
                  pranzo2,giorno3,pranzo3,giorno4,pranzo4,ritiro,parente):
    data = {'Nome': nome, 'Cognome':cognome, 'Eta':age, 'Sesso':sesso,
                'Classe':classe, 'Quota pagata':quota,
                'Intolleranze':intolleranze,'Allergie':allergie, 'Email': email,'Foto':foto,
                'Telefono1': telefono1,'Telefono2':telefono2,
                'Indirizzo':via,'Cap':cap,'Comune':comune,
                'Giorno1':giorno1,'Pranzo giorno1':pranzo1,
                'Giorno2':giorno2,'Pranzo giorno2':pranzo2,
                'Giorno3':giorno3,'Pranzo giorno3':pranzo3,
                'Giorno4':giorno4,'Pranzo giorno4':pranzo4,
                'Ritiro bimbo':ritiro,'Parentela':parente
                ,}
    nuova_riga=pd.DataFrame(data, index=[0])
    df = df.append(df, nuova_riga, ignore_index=True)
    return df

def main():


    # Titolo del form
    st.title("**Registrazione** :red[MongolCamp] :sunglasses:")
    #Bottone per scaricare csv di base
    col19, col20=st.columns(2)
    with col19:
        st.subheader('Crea file csv')
        if st.button("Crea file csv"):
            df = pd.DataFrame(columns=['Nome', 'Cognome', 'Eta', 'Sesso',
                    'Classe', 'Quota pagata',
                    'Intolleranze','Allergie', 'Email','Foto',
                    'Telefono1','Telefono2',
                    'Indirizzo','Cap','Comune',
                    'Giorno1','Pranzo giorno1',
                    'Giorno2','Pranzo giorno2',
                    'Giorno3','Pranzo giorno3',
                    'Giorno4','Pranzo giorno4',
                    'Ritiro bimbo','Parentela'])
            csv = df.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()
            href = f'<a href="data:file/csv;base64,{b64}" download="iscrizione.csv">Download file csv</a>'
            st.markdown(href, unsafe_allow_html=True)
    # Crea un pulsante per caricare il file CSV
    with col20:
        st.subheader('Carica file csv')
        uploaded_file = st.file_uploader("", type="csv")

        # Se è stato caricato un file CSV, leggilo e visualizzalo in una tabella
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            st.write(df)
        else:
            st.write(":red[Carica un file CSV per iniziare.]")
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
        ritiro = st.text_input("Nome e cognome persone autorizzate")
    with col14:
        parente= st.text_input("Legame Parentale")
    #autorizzazione foto
    with col15:
        foto = st.selectbox("Autorizzazione Foto", ["si", "no"])

    if st.button("Aggiungi"):
        df=aggiungi_riga(df,nome,cognome,age,sesso,classe,quota,intolleranze,allergie,email,foto,
                    telefono1,telefono2,via,cap,comune,giorno1,pranzo1,giorno2,
                    pranzo2,giorno3,pranzo3,giorno4,pranzo4,ritiro,parente)
        st.write(df)


if __name__ == "__main__":
    main()