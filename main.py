# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 18:27:03 2022

@author: Thierno Ibrahima CISSE
"""
import os
from pathlib import Path
from utils import dita_processing, models

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
num_keywords_missing = True
while num_keywords_missing:
    num_answers = input("\nHow many keywords do you want to extract ? ")
    if num_answers and num_answers != '0':
        try:
            num_keywords = int(num_answers)
        except ValueError:
            print("\nInvalid number of keywords")
        else:
            num_keywords_missing = False
    else:
        num_keywords = None
        num_keywords_missing = False
        print("\nThe default number of keywords (10) will be extracted")

# Choose a model between yake and bert
model_missing = True
while model_missing:
    model = (input("\nChoose between YAKE Model and BERT Model\n\n"
                   "YAKE (y) / BERT (b) : ")).lower()
    if model and model in ['y', 'b']:
        model_missing = False
    else:
        print("\nInvalid model choice")

# process in yake model
if model == 'y':
    # Getting the number of ngram for yake
    ngram_missing = True
    while ngram_missing:
        ngram_answers = input("\nWhat will be the length of the keywords ? ")
        if ngram_answers and ngram_answers != '0':
            try:
                num_ngram = int(ngram_answers)
            except ValueError:
                print("\nInvalid length for a keyword")
            else:
                ngram_missing = False
        else:
            num_ngram = None
            ngram_missing = False
            print("\nThe default length for a keyword (1-gram) will be applied")
    # list of extracted text
    corpus_list = dita_processing.strip_dita_in_directory(directory)
    corpus = ' '.join(corpus_list)
    # Extracting keywords
    print("\nYAKE EMBEDDING AND KEYWORD EXTRACTION...".center(width))
    keywords = models.yake_extractor(corpus, num_keywords, num_ngram)





