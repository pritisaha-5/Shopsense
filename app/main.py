import streamlit as st

from login import login
from dashboard import dashboard

st.set_page_config(page_title="ShopSense AI", layout="wide")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login()
    st.stop()

st.sidebar.title("🛒 ShopSense AI")

st.sidebar.success(f"Welcome {st.session_state.name}")

if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()

menu = st.sidebar.radio("Navigation", ["Dashboard"])

if menu == "Dashboard":
    dashboard()