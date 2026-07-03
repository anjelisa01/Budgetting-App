import requests
import streamlit as st

import os
from dotenv import load_dotenv
load_dotenv()

API_URL=os.getenv("API_URL")

def get_header():
    token=st.session_state.get("jwt")

    headers={
        "Content-Type":"application/json",
    }

    if token:
        headers["Authorization"]=f"Bearer {token}"
    
    return headers

def get(endpoint:str):
    return requests.get(
        f"{API_URL}{endpoint}",
        headers=get_header()
    )

def delete(endpoint:str):
    return requests.delete(
        f"{API_URL}{endpoint}",
        headers=get_header()
    )

def post(endpoint:str,json_data:dict):
    return requests.post(
        f"{API_URL}{endpoint}",
        json=json_data,
        headers=get_header()
    )

def patch(endpoint:str,json_data:dict):
    return requests.patch( 
        f"{API_URL}{endpoint}",
        json=json_data,
        headers=get_header()
        )