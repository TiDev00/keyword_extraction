"""
Line modification
-----
Utility to automatically modify couples of lines in package:
kwx/utils.py
past/builtins/misc.py
Contents:
    read lines in file
    replace lines in file
"""

with open('/usr/local/lib/python3.8/site-packages/kwx/utils.py', 'r', encoding='utf-8') as file:
    data = file.readlines()

data[330] = "    texts_no_emojis = texts_no_punctuation\n"
data[331] = ""
data[332] = ""

with open('/usr/local/lib/python3.8/site-packages/kwx/utils.py', 'w', encoding='utf-8') as file:
    file.writelines(data)

with open('/usr/local/lib/python3.8/site-packages/past/builtins/misc.py', 'r', encoding='utf-8') as file:
    data = file.readlines()

data[44] = "    from importlib import reload\n"

with open('/usr/local/lib/python3.8/site-packages/past/builtins/misc.py', 'w', encoding='utf-8') as file:
    file.writelines(data)
