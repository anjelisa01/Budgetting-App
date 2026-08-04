import streamlit as st

from services.auth import login

st.title("LOGIN")

email=st.text_input("Email: ")
password=st.text_input("Password:")

login_data={
    "email":email,
    "password":password
}

if st.button("Login"):
    res=login(login_data)

    if res.status_code == 200:
        token = res.json()["access_token"]

        st.session_state["jwt"] = token
        st.switch_page("pages/users_me.py")