


def chatbot_reply(user_input):
    
    user_input = user_input.lower()

    
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


print("Chatbot: Hello! You can say 'hello', 'how are you', or 'bye'.")

while True:
    
    user_message = input("You: ")

    
    reply = chatbot_reply(user_message)

   
    print("Chatbot:", reply)

    
    if user_message.lower() == "bye":
        break

