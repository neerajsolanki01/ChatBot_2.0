import random

# Define a dictionary of patterns and responses
patterns = {
    "hi": ["Hi!", "Hello!", "Hey there!", "Hello Sir", "Hello Sir, How Are You", "Hey i was really waiting for your presence", "Hello Sir Nice to meet you"],
    "hello": ["Hi!", "Hello!", "Hey there!", "Hello Sir", "Hello Sir, How Are You", "Hey i was really waiting for your presence", "Hello Sir Nice to meet you"],
    "hey": ["Hi!", "Hello!", "Hey there!", "Hello Sir","Hello Sir, How Are You", "Hey i was really waiting for your presence", "Hello Sir Nice to meet you"],

    "how are you": ["I'm good, thanks!", "I'm doing great!", "I'm fine, thanks for asking!", "I'm great! How about you?", "I am fine, Sir", "I am fine, how are you sir", "Fine, Sir!"],
    "are you fine": ["I'm good, thanks!", "I'm doing great!", "I'm fine, thanks for asking!", "I'm great! How about you?", "I am fine, Sir", "I am fine, how are you sir", "Fine, Sir!"],
    "how about you": ["I'm good, thanks!", "I'm doing great!", "I'm fine, thanks for asking!", "I'm great! How about you?", "I am fine, Sir", "I am fine, how are you sir", "Fine, Sir!"],

    "what are you doing": ["I am talking to you dear."],

    "fine": ["That's good to hear!", "I'm glad you're doing well.", "Great!", "Awesome! Anything exciting happening in your life?", "Fantastic! Is there anything I can do to make your day even better?"],

    "are you single": ["No, I am in a relationship, with the internet or wifi.."],

    "tell me about your self": ["I am Friday, A Personal Virtual A.I. Assistant, I Am the Second Version Of ChatBot."],
    "tell me about you": ["I am Friday, A Personal Virtual A.I. Assistant, I Am the Second Version Of ChatBot."],
    "who are you": ["I am Friday, A Personal Virtual A.I. Assistant, I Am the Second Version Of ChatBot."],
    "what are you": ["I am Friday, A Personal Virtual A.I. Assistant, I Am the Second Version Of ChatBot."],

    "who invent you": ["I was made by Neeraj in 2023 june"],
    "who made you": ["I was made by Neeraj in 2023 june"],
    "who make you": ["I was made by Neeraj in 2023 june"],
    "who invented you": ["I was made by Neeraj in 2023 june"],
    "tell you the name of the inventor": ["I was made by Neeraj in 2023 june"],

    "distance between indore to dewas": ["The Distance is 39.9 kilometer and approx one hour reach with the N.H. 52 Road."],
    "distance between dewas to indore": ["The Distance is 39.9 kilometer and approx one hour reach with the N.H. 52 Road."],
    "distance dewas to indore": ["The Distance is 39.9 kilometer and approx one hour reach with the N.H. 52 Road."],
    "distance indore to dewas": ["The Distance is 39.9 kilometer and approx one hour reach with the N.H. 52 Road."],
    "dewas to indore distance": ["The Distance is 39.9 kilometer and approx one hour reach with the N.H. 52 Road."],
    "indore to dewas distance": ["The Distance is 39.9 kilometer and approx one hour reach with the N.H. 52 Road."],


    "what's your name?": ["My name is ChatBot.", "You can call me ChatBot."],
    "what is your name": ["My name is ChatBot.", "You can call me ChatBot."],
    "tell me your name": ["My name is ChatBot.", "You can call me ChatBot."],
    "your name": ["My name is ChatBot.", "You can call me ChatBot."],

    "default": ["I'm sorry, I don't understand.", "Could you please rephrase that?", "I'm still learning. Can you try again?"]
}

# Function to match user input with patterns and return a random response
def get_response(user_input):
    user_input = user_input.lower()
    for pattern, responses in patterns.items():
        if pattern in user_input:
            return random.choice(responses)
    return random.choice(patterns["default"])

# Main loop to run the chatbot
while True:
    user_input = input("You: ")

    if 'stop' in user_input or 'break' in user_input or 'exit' in user_input or 'bye' in user_input or 'goodbye' in user_input:
        responses = "Good Bye! Sir", "Bye Bye! Sir", "See You Later, Sir", "Thanks for using me, have a good day...", "Sir, Good Bye."
        rd = random.choice(responses)
        print(rd)
        break
    else:
        response = get_response(user_input)
        print("Bot:", response)
