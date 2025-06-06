# agent2_advisor.py
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, ValidationError, constr, StringConstraints
from typing import Annotated

llm = ChatOpenAI(temperature=0.5)

class QuestionInput(BaseModel):
    question: Annotated[str, StringConstraints(strip_whitespace=True, min_length=3)]

def advise_on_question(question):
    try:
        validated = QuestionInput(question=question)
    except ValidationError as e:
        return f"Invalid question: {e}"
    prompt = f"""You are a smart, concise career coach helping a job candidate. 
Give short, specific advice on how to answer this exact interview question: 
"{validated.question}" — avoid repeating general templates."""

    return llm.invoke(prompt).content
