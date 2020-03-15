"""
Define a respond() function which takes in message as an argument, and uses the string's .endswith() method to check if a message ends with a question mark.
If the message does end with a question mark, choose a random "question" from the responses dictionary. Else, choose a random "statement" from the responses.
Send the bot multiple messages with and without a question mark - these have been provided for you. If you want to experiment further in the Shell, be sure to first hit 'Run Code'.
"""
import random

def respond(message):
    # Check for a question mark
    if message.endswith("?"):
        # Return a random question
        return random.choice(responses["question"])
    # Return a random statement
    return random.choice(responses["statement"])


# Send messages ending in a question mark
send_message("what's today's weather?")
send_message("what's today's weather?")

# Send messages which don't end with a question mark
send_message("I love building chatbots")
send_message("I love building chatbots")


