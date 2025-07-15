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

    usage_questions = [
        "how do i use this", "how does this work", "what can you do", "help me", "can you help me"
    ]

    # Match by exact phrases (case-insensitive)
    if any(re.fullmatch(phrase, query) for phrase in greetings):
        return "I am a chatbot from Adex. Ask me anything about the company."

    if any(re.fullmatch(phrase, query) for phrase in farewells):
        return "Bye, have a good day!"

    if any(re.fullmatch(phrase, query) for phrase in thanks):
        return "You're welcome!"

    if any(re.fullmatch(phrase, query) for phrase in identity_questions):
        return "I'm an AI chatbot created by Adex to answer questions about the company."

    if any(re.fullmatch(phrase, query) for phrase in usage_questions):
        return (
            "You can ask me anything about Adex, such as our services, policies, team, or documents. "
            "I'll try to find the most accurate answer using our internal knowledge."
        )

    # If no intent is matched, return None
    return None
