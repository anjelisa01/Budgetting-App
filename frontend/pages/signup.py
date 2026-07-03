import streamlit as st
import requests

from utils.api import post
from services.users import signup

# adding new user, no need auth
st.title("SIGNUP")

name=st.text_input("Name: ")
email=st.text_input("Email: ")
password=st.text_input("Password:")

signup_data={
    "name":name,
    "email":email,
    "hashed_password":password
}

if st.button("Sign Up"):
    res=signup(signup_data)
    if res.status_code==200:
        st.switch_page("pages/login.py")