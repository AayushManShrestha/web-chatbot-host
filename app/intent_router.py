import re

def detect_intent(user_input: str) -> str | None:
    query = user_input.strip().lower()

    greetings = [
        "hello", "hi", "hey",
        "who are you", "tell me about yourself",
        "what is your job", "what do you do"
    ]

    farewells = [
        "bye", "goodbye", "see you", "talk to you later"
    ]

    thanks = [
        "thanks", "thank you", "thx", "appreciate it"
    ]

    identity_questions = [
        "are you human", "are you a bot", "are you an ai", "are you real", "what are you"
    ]

    # Match by exact phrases (case-insensitive)
    if any(re.fullmatch(phrase, query) for phrase in greetings):
        return "I am a chatbot from Jasper. Ask me anything about the company."

    if any(re.fullmatch(phrase, query) for phrase in farewells):
        return "Bye, have a good day!"

    if any(re.fullmatch(phrase, query) for phrase in thanks):
        return "You're welcome!"

    if any(re.fullmatch(phrase, query) for phrase in identity_questions):
        return "I'm an AI chatbot created by Jasper to answer questions about the company."

    # If no intent is matched, return None
    return None
