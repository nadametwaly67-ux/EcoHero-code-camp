import streamlit as st

# تعريف الصفحات
home_page = st.Page(
    page="home.py",
    title="Home Page",
    icon="🏘️",
    default=True
)

signin_page = st.Page(
    page="signin.py",
    title="Sign In",
    icon="🔑"
)

signup_page = st.Page(
    page="signup.py",
    title="Sign Up",
    icon="📕"
)

chatbot_page = st.Page(
    page="chatbot.py",
    title="Chatbot",
    icon="👩‍💻"
)

# إنشاء الـ navigation bar
all_pages = st.navigation(
    pages=[home_page, signin_page, signup_page, chatbot_page],
    position="top"
)

# تشغيل الصفحات
all_pages.run()
