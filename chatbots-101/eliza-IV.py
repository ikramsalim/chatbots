"""
Get a response and phrase by calling match_rule() with the rules dictionary and message.
Check if the response is a template by seeing if it includes the string '{0}'. If it does:
Use the replace_pronouns() function on phrase.
Include the phrase by using .format() on response and overriding the value of response.
"""
# Define respond()
def respond(message):
    # Call match_rule
    response, phrase = match_rule(rules, message)
    if '{0}' in response:
        # Replace the pronouns in the phrase
        phrase = replace_pronouns(phrase)
        # Include the phrase in the response
        response = response.format(phrase)
    return response

# Send the messages
send_message("do you remember your last birthday")
send_message("do you think humans should be worried about AI")
send_message("I want a robot friend")
send_message("what if you could be anything you wanted")