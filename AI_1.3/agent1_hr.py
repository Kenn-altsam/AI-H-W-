import os
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI  # <- NEW import

llm = ChatOpenAI(
    temperature=0.7,
    openai_api_key=os.getenv("OPENAI_API_KEY")  # <- EXPLICIT KEY PASSING
)

from langchain.prompts import PromptTemplate

prompt = PromptTemplate.from_template("Ask a behavioral job interview question about {topic}.")

def get_question(topic="teamwork"):
    question = prompt.format(topic=topic)
    return llm.invoke(question).content
