import streamlit as st
import requests

API_URL="https://friendly-doodle-x5wp79r55w9wfpj4x-8000.app.github.dev"

title=st.text_input("title")
amount=st.text_input("amount")
note=st.text_input("note")
user_id=st.text_input("user_id")

user_id=int(user_id)
amount=float(amount)

transaction_data={
    "title":title,
    "amount":amount,
    "note":note,
    "user_id":user_id
}

if st.button("Add transaction"):
    res=requests.post(f"{API_URL}/transactions",json=transaction_data)
    print("Status:", res.status_code)
    st.write(res.text)