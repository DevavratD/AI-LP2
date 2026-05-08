import random


class ChatBot:
    def __init__(self):

        # in exam make more responses and keywords to make the chatbot more interactive and engaging.
        self.responses = {
            ("hi", "hello", "hey"): ["Hello!", "Hi there!", "Hey!"],
            ("how are you", "how are you doing"): [
                "I am fine.",
                "Doing great!",
                "All good.",
            ],
            ("what is your name", "who are you"): ["I am PyBot.", "My name is PyBot."],
            ("bye", "goodbye"): ["Goodbye!", "See you soon!"],
            ("python",): ["Python is a programming language."],
            ("ai", "artificial intelligence"): [
                "AI is simulation of human intelligence."
            ],
        }

    # Find Best Response
    def getResponse(self, userInput):

        userInput = userInput.lower()

        for keywords, replies in self.responses.items():
            for word in keywords:
                if word in userInput:
                    return random.choice(replies)

        return "Sorry, I do not understand."


# Create Bot
bot = ChatBot()

print("ChatBot: Hello! Type 'bye' to exit.\n")

while True:
    user = input("You: ")

    response = bot.getResponse(user)

    print("ChatBot:", response)

    if user.lower() == "bye":
        break
