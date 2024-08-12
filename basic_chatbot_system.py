responses = {
    "hi": "Hello!",
    "hello": "Hi there!",
    "what is your name": "I'm just a chatbot",
    "how are you": "I'm good",
    "thanks": "No problem",
    "quit": "Goodbye, see you later",
}


def chatbot():
    print("Hi! I'm your chatbot. Type 'quit' to exit.")

    while True:
        user_input = input("> ").lower()

        if user_input in responses:
            print(responses[user_input])
            if user_input == "quit":
                break
        else:
            print("I'm sorry, I don't understand that.")


if __name__ == "__main__":
    chatbot()
