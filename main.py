import pandas as pd
import streamlit as st



if "selected_tab" not in st.session_state:
    st.session_state.selected_tab = "2"

data = pd.read_excel("User & Pass.xlsx", "Sheet1")

staff_members = list(data["USERNAME"])
staff_passwords = list(data["PASSWORD"])

if st.session_state.selected_tab == "2":
    a = st.radio("", options=("Student", "Staff"), horizontal=True)

    if a == "Student":
        st.header("Welcome Student!")
    if a == "Staff":
        st.header("Welcome Staff!")

    with st.form("Form 1", clear_on_submit=False):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")

        if submitted:
            if a == "Staff":
                if username in staff_members and password in staff_passwords:
                    st.success("Click login again..")
                    st.session_state.selected_tab = "1"
                else:
                    st.error("Invalid username or password")

elif st.session_state.selected_tab == "1":
    st.header("")
    st.title("Ruko bhai abhi to website ban rahi hee 😂")
    
