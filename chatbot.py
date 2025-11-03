def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello there! How can I help you today?"
    elif "your name" in user_input:
        return "I’m ChatBuddy, your friendly chatbot!"
    elif "how are you" in user_input:
        return "I’m just code, but I’m doing great 😄"
    elif "joke" in user_input:
        return "Why did the computer show up at work late? Because it had a hard drive! 😂"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "Hmm... I didn’t quite get that. Can you say it differently?"
