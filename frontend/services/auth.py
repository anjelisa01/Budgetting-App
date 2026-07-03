import requests

from utils.api import post

def login(login_data):
    res=res=post("/api/v1/auth/login",login_data)
    return res