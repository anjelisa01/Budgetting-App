#imports
import streamlit as st
import pandas as pd

from services.users import get_user,update_user,delete_user
from utils.auth import require_auth

#confirm authentication
user = require_auth()

st.title("This is User's page")
st.text("User can see, update and delete their account here")

tab1,tab2,tab3=st.tabs(["Your Data","Update your data","Delete Account"])

with tab1:
    data=get_user()
    df=pd.DataFrame([data])
    st.header("User data")
    st.dataframe(df)

with tab2:
    name=st.text_input("Name: ",value=user['name'])
    email=st.text_input("Email: ",value=user['email'])
    password=st.text_input("New Password:")

    data={
        "name":name,
        "email":email,
        "password":password
    }

    if st.button("Update data"):
        res=update_user(data)
        if res.ok:
            st.rerun() 
    
@st.dialog("Confirmation")
def confirm_dialog():
    st.write("Are you sure you want to continue?")
    if st.button("Yes"):
        st.success("Account deleted!")
        res=delete_user()
        if res.status_code==200:
            st.session_state.pop("jwt",None)
            st.switch_page("pages/auth_login.py")
    if st.button("Cancel"):
        st.rerun()

with tab3:
    if st.button("Delete account"):
        confirm_dialog()