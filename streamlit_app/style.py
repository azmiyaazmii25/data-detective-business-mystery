import streamlit as st

def apply_style():
    st.markdown("""
        <style>

        /* Background */
        .stApp {
            background-color: #0e1117;
            color: #ffffff;
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background-color: #111827;
        }

        /* Metric boxes */
        div[data-testid="metric-container"] {
            background-color: #1f2937;
            padding: 15px;
            border-radius: 10px;
        }

        /* Titles */
        h1, h2, h3 {
            color: #facc15;
        }

        </style>
    """, unsafe_allow_html=True)