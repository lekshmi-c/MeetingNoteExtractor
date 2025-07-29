import whisper
import tempfile

model = whisper.load_model("base")  # or "medium", "large" for better accuracy

def transcribe_audio(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name
    result = model.transcribe(tmp_path)
    return result["text"]
