import streamlit as st
import requests
import pandas as pd

# API_URL=

if "jwt" not in st.session_state:
    st.switch_page("login.py")

if st.button(f"See all transactions"):
    response=requests.get(f"{API_URL}/transactions")
    data=response.json()

    df=pd.DataFrame(data)

    st.header("All transactions data")
    st.dataframe(df)