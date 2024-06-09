import streamlit as st
from utils import inject_sidebar_logo


st.set_page_config(
    page_title="Procurement Home",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="expanded",
)

logo_path = "logo.png"
inject_sidebar_logo(logo_path)

# Function to inject CSS for the sidebar logo
