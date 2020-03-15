"""
Get a response and phrase by calling match_rule() with the rules dictionary and message.
Check if the response is a template by seeing if it includes the string '{0}'. If it does:
Use the replace_pronouns() function on phrase.
Include the phrase by using .format() on response and overriding the value of response.
"""
""" RULES DICT
('do you think (.*)', ['if {0}? Absolutely.', 'No chance'])
('do you remember (.*)', ['Did you think I would forget {0}', "Why haven't you been able to forget {0}", 'What about {0}', 'Yes .. and?'])
('I want (.*)', ['What would it mean if you got {0}', 'Why do you want {0}', "What's stopping you from getting {0}"])
('if (.*)', ["Do you really think it's likely that {0}", 'Do you wish that {0}', 'What do you think about {0}', 'Really--if {0}'])
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