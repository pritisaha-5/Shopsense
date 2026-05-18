import streamlit as st
import pandas as pd

def show_insights():

    st.title("📊 Business Insights")

    df = pd.read_csv("data/processed/cleaned_data.csv")

    st.write("Top States")
    st.write(df["customer_state"].value_counts().head(10))

    st.write("Payment Types")
    st.write(df["payment_type"].value_counts())