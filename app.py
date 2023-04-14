from funzioni import somma_due_numeri
import streamlit as st

def area_triangolo(a,b):
    '''questa funzione calcola area di un triangolo con base e altezza'''
    area = (a*b)/2
    return area
def somma_due_numeri(a,b):
    return a+b

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://www.artemedialab.it/wp-content/uploads/2019/04/immagini-sfondo-1.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )


def main():

    st.latex(r'''
        a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
        \sum_{k=0}^{n-1} ar^k =
        a \left(\frac{1-r^{n}}{1-r}\right)
        ''')
    
    x1 = st.slider('Please inserisci base', 0, 100, 25)
    x2 = st.slider('Please inserisci altezza', 0, 100, 35)
    
    if st.button('calcola area triancolo', help="Click here"):

        area=area_triangolo(x1,x2)
        st.write(f"l'area del triangolo è {area}")


    input = st.number_input("inserisci base", 0)
    input1 = st.number_input("inserisci altezza", 0)
    st.write(area_triangolo(input,input1))

    add_bg_from_url()
if __name__ == "__main__":
    main()

