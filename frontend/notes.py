import streamlit as st

def render_ui():
    uploaded_file = st.file_uploader("Upload Meeting Audio (.mp3/.wav)", type=["mp3", "wav"])
    return uploaded_file
