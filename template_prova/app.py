import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def main():
    
    st.title("Template")
    generate_random = np.random.RandomState(667)
    n = st.slider("inserisci numero di punti", min_value=1, max_value=1000)
    x = 10 * generate_random.rand(n)

    dev_standard = st.slider("inserisci il rumore", min_value=0,max_value=10)

    noise = np.random.normal(0, dev_standard, n)

    y = 3 * x + noise
    X = x.reshape(-1,1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size = 0.2, 
                                                    random_state = 667
                                                    )
    model = LinearRegression(fit_intercept=True)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    length = y_pred.shape[0] #  
    x = np.linspace(0,length,length)

    fig1=plt.figure(figsize=(8,6))
    plt.plot(x, y_test, label='real y')
    plt.plot(x, y_pred, label="predicted y'")
    plt.legend(loc=2)
    plt.grid()
    st.write(fig1)
    
    fig = plt.figure(figsize = (10, 8))

    plt.scatter(X_train, y_train,label='Training_set')
    plt.scatter(X_test, y_test,color='orange',label='Test_set')
    plt.plot(X_test, y_pred,color='red',label='regression line')
    plt.xlabel('cose')
    plt.ylabel('cose2')
    plt.legend()
    plt.grid()
    st.write(fig)
if __name__ == "__main__":
    main()