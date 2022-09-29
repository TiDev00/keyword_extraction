# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 18:27:03 2022

@author: Thierno Ibrahima CISSE
"""
import os
from pathlib import Path

if __name__ == "__main__":
    # get the terminal width
    width = os.get_terminal_size().columns

    # clear terminal before displaying program
    os.system('cls' if os.name == 'nt' else 'clear')

    # Displaying = according to terminal width
    equal_sign = "=" * width

    title = "WELCOME TO THE KEYWORD EXTRACTOR !"

    # Composed by the equal_sign and title
    header = equal_sign + "\n\n" + title.center(width) + "\n\n" + equal_sign + "\n"
    print(header)

# Wrap given path in Path object and verify if it exists on mac or windows.
# Expanduser will allow to interpret ~ in path as home dir
isNotDirectory = True
while isNotDirectory:
    directory = Path(os.path.expanduser(input("Enter path to a directory containing dita files : ")))
    if os.path.exists(directory):
        isNotDirectory = False
    else:
        print("\nInvalid path\n")

