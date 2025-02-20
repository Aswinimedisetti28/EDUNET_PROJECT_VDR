import streamlit as st

def show():
    st.markdown("<h1 style='text-align: center;'>💎 Your Try-On Results</h1>", unsafe_allow_html=True)
    st.image("https://source.unsplash.com/800x400/?fashion-preview", use_container_width=True)
    st.success("✨ You look amazing! Ready to shop?")
