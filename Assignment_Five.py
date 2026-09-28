# Assignment Five for Python - Arush Mahajan (Div:13)

import re

text = input("Enter anything: ")

not_chars = re.findall("[^a-zA-Z0-9]", text)

if len(text) == 0:
    print("Input is empty.")
elif len(not_chars) > 0:
    print("It has special characters")
else:
    print("Only letters and numbers.")
