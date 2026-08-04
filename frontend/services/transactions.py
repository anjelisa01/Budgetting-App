import requests
#import utils
from utils.api import post,get,patch,delete #crud api

def get_all_transactions():
    response=get("/api/v1/transactions/")
    data=response.json()
    return data #this is a json, change to df to destination

def add_new_transactions(data):
    response=post("/api/v1/transactions/",data)
    return response


def get_one_transaction(id):
    response=get(f"/api/v1/transactions/{id}")
    data=response.json()
    return data

def update_transaction(id,data):
    response=patch(f"/api/v1/transactions/{id}",data )
    return response

def delete_transaction(id):
    response=delete(f"/api/v1/transactions/{id}" )
    return response
    