#!/usr/bin/python3
"""
mood.py

This program takes the user's mood as input
and prints some message to encourage them
based on some keyword in their input.

Usage example:
    run: ./mood.py
    > How do you feel today? 
    I feel good.

# based on the keyword `good` the program should print
    I am glad, you're feeling good.
"""

import random

print(__doc__)

mood = input("> ")

# split words in `mood` to have a list of `words`
words = mood.split()
# Filter words to have each word only once
words = set(words)

# list of responses
good = [
        " I am glad",
        " that's a good thing",
        "I am so happy for you",
        "Lol.. Looks like you're having a good day"
        ]
# conditional statements and print some messages based on user input
for word in words:
    if "good" in word.lower():
        print(random.choice(good))
    elif "bad" in word.lower():
        print("Sorry about that. Well, it happens, so cheer up" \
                 "and you'll be fine in the end.")
    elif "sick" in word.lower():
        print("Get well soon. Try to get treatment " \
                "check on your doctor for advise.")

