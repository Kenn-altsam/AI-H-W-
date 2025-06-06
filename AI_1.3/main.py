import random
from agent1_hr import get_question
from agent2_advisor import advise_on_question

topics = [
    "teamwork", "failure", "leadership", "conflict resolution", "adaptability",
    "problem solving", "communication", "decision making", "time management",
    "initiative", "stress management", "attention to detail", "work ethic",
    "handling criticism", "collaboration", "meeting deadlines", "motivation",
    "multitasking", "goal setting", "creativity"
]

def run_a2a():
    selected_topics = random.sample(topics, k=5)  # pick 5 random topics
    for topic in selected_topics:
        print("\n==============================")
        print(f"🎯 Topic: {topic}")
        question = get_question(topic)
        print(f"🤖 HR Agent: {question}")
        advice = advise_on_question(question)
        print(f"🧠 Advisor: {advice}")

if __name__ == "__main__":
    run_a2a()
