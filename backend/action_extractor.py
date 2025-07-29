from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama

llm = Ollama(model="llama2")  # You can replace with mistral, phi, etc.
print(llm.invoke("What is LangChain?"))
def extract_action_items(transcript):
    prompt_template = PromptTemplate.from_template("""
    Extract all the action items and tasks from the following meeting transcript.
    Return them as a checklist format:

    Transcript:
    {transcript}

    Checklist:
    """)
    
    prompt = prompt_template.format(transcript=transcript)
    return llm(prompt)



# ##################OpenAI API code ==========================================

# import openai
# import os
# from dotenv import load_dotenv 
# load_dotenv()  # Load .env file
# openai.api_key = os.getenv("OPENAI_API_KEY")

# def extract_action_items(transcript):
#     prompt = f"""Extract all the action items and tasks from the following meeting transcript. Return as a checklist format:\n\n{transcript}"""

#     response = openai.ChatCompletion.create(
#         model="gpt-4",
#         messages=[
#             {"role": "user", "content": prompt}
#         ]
#     )
#     return response['choices'][0]['message']['content']
