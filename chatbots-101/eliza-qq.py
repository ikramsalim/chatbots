"""ELIZA II: Extracting key phrases
The really clever thing about ELIZA is the way the program appears to understand what you told it by occasionally including phrases uttered by the user in its responses.

In this exercise, you will match messages against some common patterns and extract phrases using re.search(). A dictionary called rules has already been defined, which matches the following patterns:

"do you think (.*)"
"do you remember (.*)"
"I want (.*)"
"if (.*)"
Inspect this dictionary in the Shell before starting the exercise.

"""


# Define match_rule()
def match_rule(rules, message):
    response, phrase = "default", None

    # Iterate over the rules dictionary
    for pattern, responses in rules.items():
        # Create a match object
        match = re.search(pattern, message)
        if match is not None:
            # Choose a random response
            response = random.choice(responses)
            if '{0}' in response:
                phrase = match.group(1)
    # Return the response and phrase
    return response, phrase


# Test match_rule
print(match_rule(rules, "do you remember your last birthday"))