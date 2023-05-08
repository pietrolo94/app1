import streamlit as st
import numpy as np  
import pandas as pd
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def main():
    
    st.title("Template")
    df =pd.read_csv("Startup.csv")
    st.write(df)
    X = df.drop(columns="Profit")
    y = df["Profit"]
    model = LinearRegression(fit_intercept=True)
    model.fit(X, y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size = 0.2, 
                                                    random_state = 667
                                                    )
    y_pred = model.predict(X_test)
    length = y_pred.shape[0] #  
    x = np.linspace(0,length,length)

    fig=plt.figure(figsize=(8,5))
    plt.plot(x, y_test, label='real y')
    plt.plot(x, y_pred, label="predicted y'")
    plt.legend(loc=2)
    st.write(fig)
    rd = st.number_input("R&D spend", value= 0.0)
    amm = st.number_input("administration", value=0.0)
    mark = st.number_input("Marketing", value=0.0)
    res = model.predict([[rd, amm, mark]])[0]
    st.write(f"predicted profit {round(res,1)}")
if __name__ == "__main__":
    main()