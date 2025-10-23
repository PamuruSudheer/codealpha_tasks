# --- Simple Rule-Based Chatbot ---

# Step 1: Define a function for chatbot responses
def chatbot_reply(user_input):
    # Convert input to lowercase (to make matching easier)
    user_input = user_input.lower()

    # Step 2: Use if-elif-else to decide response
    if user_input == "hello":
        return "hi!"
    elif user_input == "how are you":
        return "i'm fine, thanks!"
    elif user_input == "hi":
        return "hi!"
    elif user_input =="good morning" or user_input =="good evening":
        return "good morning" or "good evening "
    elif user_input =="nice to chat with you":
        return "same to you"
    elif user_input == "bye":
        return "Goodbye"
    else:
        return "I don't understand that."

# Step 3: Main chat loop
print("Chatbot: Hello! You can say 'hello', 'how are you', or 'bye'.")

while True:
    # Get input from user
    user_message = input("You: ")

    # Get chatbot's reply
    reply = chatbot_reply(user_message)

    # Print chatbot's reply
    print("Chatbot:", reply)

    # If user says 'bye', end the chat
    if user_message.lower() == "bye":
        break
