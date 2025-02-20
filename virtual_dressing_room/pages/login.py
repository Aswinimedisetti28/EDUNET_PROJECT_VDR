import streamlit as st

def show():
    st.markdown("<h1 style='text-align: center;'>🔐 Login / Register</h1>", unsafe_allow_html=True)

    login_col, register_col = st.columns(2)

    with login_col:
        st.subheader("Existing Users")
        username = st.text_input("👤 Username")
        password = st.text_input("🔑 Password", type="password")
        if st.button("Login"):
            st.success(f"✅ Welcome, {username}!")

    with register_col:
        st.subheader("New Users")
        new_user = st.text_input("👤 Create Username")
        new_pass = st.text_input("🔑 Create Password", type="password")
        if st.button("Register"):
            st.success("✅ Registration Successful!")
