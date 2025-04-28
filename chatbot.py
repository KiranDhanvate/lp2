# Define bot responses with fixed choices
responses = {
    "greeting": ["Hello! Welcome to our store. How can I help you today?", 
                 "Hi there! What can I do for you?"],
    
    "hours": ["We're open Monday to Friday, 9am to 7pm, and Saturday 10am to 5pm.", 
              "Our store hours are weekdays 9-7 and Saturdays 10-5."],
    
    "location": ["We're located at 123 Main Street, Downtown.", 
                 "Our address is 123 Main Street in the city center."],
    
    "returns": ["We accept returns within 30 days with a receipt.", 
                "You can return items within 30 days if you have the original receipt."],
    
    "products": ["We carry a wide range of electronics, home goods, and clothing.", 
                 "Our inventory includes electronics, home items, and apparel."],
    
    "goodbye": ["Thank you for visiting! Have a great day!", 
                "Goodbye! Come back soon!"],
    
    "default": ["I'm sorry, I didn't understand that. Could you rephrase?", 
                "I'm not sure I follow. Could you ask another way?"]
}

# Keyword matching for responses
keywords = {
    "hi": "greeting",
    "hello": "greeting",
    "hey": "greeting",
    "hours": "hours",
    "open": "hours",
    "close": "hours",
    "location": "location",
    "address": "location",
    "where": "location",
    "return": "returns",
    "exchange": "returns",
    "product": "products",
    "item": "products",
    "sell": "products",
    "bye": "goodbye",
    "goodbye": "goodbye",
    "thanks": "goodbye"
}

# Simple response selector that alternates between options
response_index = 0

def get_response(user_input):
    global response_index
    user_input = user_input.lower()
    
    # Check for keywords
    for word in keywords:
        if word in user_input:
            # Get the response list for this keyword
            response_list = responses[keywords[word]]
            # Select response using simple alternation
            selected = response_list[response_index % len(response_list)]
            response_index += 1
            return selected
    
    # Default response if no keywords matched
    default_responses = responses["default"]
    selected = default_responses[response_index % len(default_responses)]
    response_index += 1
    return selected

# Main chat loop
print("Bot: " + responses["greeting"][0])
response_index += 1

while True:
    user_input = input("You: ")
    if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
        print("Bot: " + responses["goodbye"][response_index % len(responses["goodbye"])])
        break
    response = get_response(user_input)
    print("Bot: " + response)
