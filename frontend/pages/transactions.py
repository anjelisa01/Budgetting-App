import streamlit as st
import pandas as pd
import time

from services.transactions import get_all_transactions,add_new_transactions, get_one_transaction,update_transaction,delete_transaction
from utils.auth import require_auth

#confirm authentication
user = require_auth()

# st.button(f"See all transactions")

st.title("TRANSACTIONS Page")
tab1,tab2=st.tabs(["Your Transaction","Add  transaction"])

with tab1:
    data=get_all_transactions()
    df=pd.DataFrame(data)
    st.header("Transaction data")
    st.dataframe(df)

    with st.expander('update'):
        update_id=st.number_input("Id transaction to update: ")
        if st.button("i want to update"):
            transaction=get_one_transaction(update_id)

            # transaction_type=st.radio("Transaction Type:",
            #         ["Expense", "Income"])
            title=st.text_input("Title: ",value=transaction['title'])
            amount=st.number_input("Amount: ")
            note=st.text_input("Note:")
        
        # if st.button("Update Transaction: "):
        #     pass


    with st.expander('delete'):
        delete_id=st.number_input("id transaction to delete: ")
        if st.button("Delete Transaction: "):
            pass


with tab2:
    
    transaction_type=st.radio("Transaction Type:",
    ["Expense", "Income"])
    title=st.text_input("Title: ")
    amount=st.number_input("Amount: ")
    note=st.text_input("Note:")

    data={
        "title":title,
        "amount":amount,
        "note": note,
        "transaction_type": transaction_type.lower()
    }
    
    if st.button("Add Transaction: "):
        res=add_new_transactions(data)
        if res.ok:
            st.success("✅ Item added!")
            time.sleep(1)

            st.rerun() 
        










# # Editable table
# edited_df = st.data_editor(
#     df,
#     num_rows="dynamic",   # allows adding/removing rows
#     use_container_width=True
# )

# # Save button
# if st.button("Save Changes"):
#     # Here you can save to CSV, database, etc.
#     st.success("Data saved successfully!")

# with st.popover("➕ Add Data"):
#     with st.form("form"):
#         name = st.text_input("Name")
#         age = st.number_input("Age")

#         if st.form_submit_button("Save"):
#             st.success("Saved!")



#     # response=requests.get(f"{API_URL}/transactions")
#     # data=response.json()

#     # df=pd.DataFrame(data)

#     # st.header("All transactions data")
#     # st.dataframe(df)