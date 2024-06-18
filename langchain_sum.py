from dotenv import load_dotenv
from langchain import OpenAI
import os


load_dotenv()


def summarize_text(text):
    llm = OpenAI(temperature=0, openai_api_key = os.environ.get('OPENAI_API_KEY'))
    prompt = f"Provide a comprehensive summary of the given text: {text}"
    text =  llm(prompt)
    return text
    

