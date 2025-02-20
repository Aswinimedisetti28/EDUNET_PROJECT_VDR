import streamlit as st

def show():
    st.markdown("<h1 style='text-align: center;'>🛍️ Welcome to VirtuFit - AI Dressing Room</h1>", unsafe_allow_html=True)
    
    st.write("""
    **Why use an AI Virtual Dressing Room?**
    - 👕 Try on clothes virtually using AI.
    - 📸 Use a live camera or upload an image.
    - 🤖 AI detects body & applies clothing automatically.
    - 🛍️ Save time & shop smarter.
    """)

    st.image("assets/background.jpg", use_container_width=True)

    st.markdown("### 📌 Project Features")
    st.write("""
    - **Live Camera Integration**
    - **Real-Time Clothing Selection**
    - **AI-Powered Fit Recommendation**
    - **User-Friendly Navigation & Login System**
    """)

    st.image("assets/project_structure.jpg", use_container_width=True)
