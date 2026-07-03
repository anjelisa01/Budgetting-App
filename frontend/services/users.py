import requests
#import utils
from utils.api import post,get,patch,delete #crud api

def signup(signup_data):
    res=post("/api/v1/users/signup",signup_data)
    return res

def get_user():
    response=get("/api/v1/users/me")
    data=response.json()
    return data #this is a json, change to df to destination

def update_user(update_data):
    res=patch("/api/v1/users/me",update_data)
    return res

def delete_user():
    res=delete("/api/v1/users/me")
    return res