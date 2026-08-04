import streamlit as st
import pandas as pd

# Example dataframe
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "London", "Paris"]
})

st.title("Editable Data Table")

# Editable table
edited_df = st.data_editor(
    df,
    num_rows="dynamic",   # allows adding/removing rows
    use_container_width=True
)

# Save button
if st.button("Save Changes"):
    # Here you can save to CSV, database, etc.
    edited_df.to_csv("updated_data.csv", index=False)
    st.success("Data saved successfully!")


# #disable id 
# edited_df = st.data_editor(
#     df,
#     disabled=["ID"],
#     use_container_width=True
# )



import sqlite3

if st.button("Save to Database"):
    conn = sqlite3.connect("database.db")
    edited_df.to_sql("my_table", conn, if_exists="replace", index=False)
    conn.close()

    st.success("Database updated!")