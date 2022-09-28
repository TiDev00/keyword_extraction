"""
DITA Files
-----
Function for extracting text in dita file.
Contents:
    strip_dita_text
"""
import os
from bs4 import BeautifulSoup


def strip_dita_text(file):
    """
        Load a dita file and extract text within the file without the tags
        Parameters
        ----------
            file : dita or xml
                File from which the text will be extracted
        Returns
        -------
            text : str
                String of extracted text from dita file
    """
    return (BeautifulSoup(file, features='xml')).get_text()


def strip_dita_in_directory(directory):
    """
        Use the strip_dita_text function in a for multiple files in a directory
        and return the list of extracted text
        Parameters
        ----------
            directory : path
                Directory which contains a set of dita or xml files
        Returns
        -------
            list_text : list
                List of text extracted from each file
    """
    list_of_docs = []
    for root, subdirectories, files in os.walk(directory):
        for file in files:
            if os.path.join(root, file).endswith('.dita'):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    print("--------------------- " + file + " ---------------------")
                    print("Extracting text in file...")
                    text = strip_dita_text(f)
                    f.close()
                list_of_docs.append(text)
    return list_of_docs
