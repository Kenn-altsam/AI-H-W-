# main.py
from agent1_hr import get_question
from agent2_advisor import advise_on_question

def run_a2a():
    topics = ["teamwork", "failure", "leadership"]
    for topic in topics:
        print("\n==============================")
        print(f"🎯 Topic: {topic}")
        question = get_question(topic)
        print(f"🤖 HR Agent: {question}")

        advice = advise_on_question(question)
        print(f"🧠 Candidate Advisor: {advice}")

if __name__ == "__main__":
    run_a2a()
