import streamlit as st

# 🌟 Set Page Config
st.set_page_config(page_title="🛍️ VirtuFit - AI Dressing Room", layout="wide")

# 📌 Load CSS for Custom Styling
with open("assets/navbar.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# 📌 Sidebar Navigation
st.sidebar.image("assets/user_icon.png", width=80)
st.sidebar.title("🔍 Navigation")
page = st.sidebar.radio("Go to:", ["🏠 Home", "🔐 Login/Register", "👕 Try Clothes", "📸 Results", "🚪 Logout"])

# 📌 Load Selected Page
if page == "🏠 Home":
    from pages import home
    home.show()
elif page == "🔐 Login/Register":
    from pages import login
    login.show()
elif page == "👕 Try Clothes":
    from pages import tryon
    tryon.show()
elif page == "📸 Results":
    from pages import results
    results.show()
elif page == "🚪 Logout":
    from pages import logout
    logout.show()
