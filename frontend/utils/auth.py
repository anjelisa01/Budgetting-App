# The idea behind utils/auth.py is that every protected page calls the same function instead of repeating auth checks everywhere.

import streamlit as st
from utils.api import get

def require_auth():
    token=st.session_state.get("jwt") #get token from session_state

    if not token: #if there is none
        st.switch_page("pages/login.py")

    #verify with fastapi
    response=get("/api/v1/users/me")

    #if token invalid/expired
    if response.status_code!=200:
        st.session_state.pop("jwt",None)
        st.switch_page("pages/login.py")
    
    return response.json()
