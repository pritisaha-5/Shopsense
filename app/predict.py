import streamlit as st
import numpy as np
import joblib

def show_predict():

    st.title("🔍 Churn Prediction")

    model = joblib.load("models/churn_model.pkl")

    recency = st.number_input("Recency", value=100)
    frequency = st.number_input("Frequency", value=2)
    monetary = st.number_input("Monetary", value=200.0)

    if st.button("Predict"):

        features = np.array([[recency, frequency, monetary]])

        prediction = model.predict(features)[0]
        prob = model.predict_proba(features)[0][1]

        if prediction == 1:
            st.error(f"⚠ High Risk ({prob:.2%})")
        else:
            st.success(f"✅ Low Risk ({prob:.2%})")