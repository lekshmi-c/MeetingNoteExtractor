from transformers import pipeline


summarizer_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_summary(transcript):
    summary = summarizer_pipeline(transcript, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']






############### using openAI############
# import openai
# import os
# from dotenv import load_dotenv

# load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")

# def generate_summary(transcript):
#     response = openai.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant that summarizes meeting transcripts."},
#             {"role": "user", "content": transcript}
#         ]
#     )
#     return response.choices[0].message.content.strip()



