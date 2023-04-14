from funzioni import somma_due_numeri
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from numpy.random import rand
import math
from streamlit.components.v1 import components

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

def formula_di_erone(a,b,c):
    if a<(b+c) and b<(a+c) and c<(a+b):
        p=(a+b+c)/2
        area=math.sqrt(p*(p-a)*(p-b)*(p-c))
        return area
    else:
        return None

def upload_video():
    video = st.file_uploader("gian.modificato.mp4", type=["mp4"])
    if video is not None:
        st.video(video)

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


    input = st.number_input("inserisci lato 1", 0.0)
    input1 = st.number_input("inserisci lato 2", 0.0)
    input2 = st.number_input("inserisci lato 3",0.0)
    area = formula_di_erone(input,input1,input2)
    if area != None:
        st.write(f"l'area del triangolo è {area}")
    else:
        "non hai inserito i segmenti di un triangolo"
    

    
if __name__ == "__main__":
    main()

