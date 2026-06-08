import streamlit as st
import requests
import pandas as pd

API_URL="https://friendly-doodle-x5wp79r55w9wfpj4x-8000.app.github.dev"


if st.button(f"See all transactions"):
    response=requests.get(f"{API_URL}/transactions")
    data=response.json()

    df=pd.DataFrame(data)

    st.header("All transactions data")
    st.dataframe(df)