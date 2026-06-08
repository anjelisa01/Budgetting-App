import streamlit as st
import requests

API_URL="https://friendly-doodle-x5wp79r55w9wfpj4x-8000.app.github.dev"

st.title("FastAPI_Streamlit")

# users=st.Page("users.py",title="Users")
# pg=st.navigation([users])
# pg.run()

name=st.text_input("Name: ")
email=st.text_input("Email: ")

signup_data={
    "name":name,
    "email":email
}

if st.button("Sign Up"):
    res=requests.post(f"{API_URL}/signup",json=signup_data)
    print("Status:", res.status_code)
    st.write(res.text)