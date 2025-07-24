#import libraries
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

#define class
class GROQLLM:
    def __init__(self):
        load_dotenv(override=True)
        self.groq_api_key=os.getenv('GROQ_API_KEY')
        if not self.groq_api_key:
            raise ValueError("ERROR:GROQ API KEY is not set in enviroment variable")
        
    #define method the call llm

    def get_llm(self):
        try:
            llm=ChatGroq(groq_api_key=self.groq_api_key,model='llama-3.1-8b-instant')
            return llm
        except Exception as e:
            raise ValueError(f"error occured while initializing llm :{e}")
        



