"""
Line modification
-----
Utility to automatically modify couples of lines in package kwx/utils.py
Contents:
    read lines in file
    replace lines in file
"""

with open('kwx/utils.py', 'r', encoding='utf-8') as file:
    data = file.readlines()

data[330] = "\ttexts_no_emojis = texts_no_punctuation\n"
data[331] = ""
data[332] = ""

with open('kwx/utils.py', 'w', encoding='utf-8') as file:
    file.writelines(data)
