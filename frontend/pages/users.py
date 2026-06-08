import streamlit as st

# signup=st.Page("signup.py",title="Signup")

st.title("This is users page")

import requests
import pandas as pd

API_URL="https://friendly-doodle-x5wp79r55w9wfpj4x-8000.app.github.dev"

user_id=st.text_input("user_id")

if st.button(f"See data user"):
    user_id=int(user_id)
    response=requests.get(f"{API_URL}/users/me/{user_id}")
    data=response.json()

    df=pd.DataFrame([data])

    st.header("User data")
    st.dataframe(df)