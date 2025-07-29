import streamlit as st
from frontend.notes import render_ui
from backend.transcription import transcribe_audio
from backend.summarizer import generate_summary
from backend.action_extractor import extract_action_items
from dotenv import load_dotenv
load_dotenv()


st.set_page_config(page_title="Meeting Notes Extractor", layout="wide")

def main():
    st.title("🎙️ Meeting Notes & Action Items Extractor")
    uploaded_file = render_ui()

    if uploaded_file:
        st.info("Processing audio...")
        transcript = transcribe_audio(uploaded_file)
        st.subheader("📝 Transcript")
        st.text_area("Transcript", transcript, height=300)

        st.subheader("📄 Summary")
        summary = generate_summary(transcript)
        st.write(summary)

        st.subheader("✅ Action Items")
        action_items = extract_action_items(transcript)
        st.write(action_items)

if __name__ == "__main__":
    main()
