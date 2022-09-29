# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 18:27:03 2022

@author: Thierno Ibrahima CISSE
"""
import os
from pathlib import Path
import utils

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
directory_missing = True
while directory_missing:
    directory_response = input("Enter a path to a directory with dita files : ")
    if directory_response:
        directory = Path(os.path.expanduser(directory_response))
        if os.path.exists(directory):
            directory_missing = False
        else:
            print("\nInvalid path\n")
    else:
        print("\nInvalid path\n")

# Number of keywords wanted
num_keyword_missing = True
while num_keyword_missing:
    try:
        num_keywords = int(input("\nHow many keywords do you want to extract ? "))
    except ValueError:
        print("\nInvalid number of keywords")
    else:
        num_keyword_missing = False

# Choose a model between yake and bert
model_missing = True
while model_missing:
    model = (input("\nChoose between YAKE Model and BERT Model\n\n"
                   "YAKE (y) / BERT (b) : ")).lower()
    if model and model in ['y', 'b']:
        model_missing = False
    else:
        print("\nInvalid model choice")

if model == 'y':
    ngram_missing = True
    while ngram_missing:
        try:
            keywords_length = int(input("\nWhat is the length of extracted keywords ? "))
        except ValueError:
            print("\nInvalid keyword length")
        else:
            ngram_missing = False


