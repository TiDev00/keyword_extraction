# DITA Keywords Extraction Tool

## Description
Useful tool to extract keyword for multiple dita files. 
It is based on Unsupervised Approach for Automatic 
Keyword Extraction using Text Features. Yake and kwx are 
used for the extracting model.

## Installation
The list of needed packages with there specific version is 
in the requirements.txt file. Run the following command to 
install them.
```
pip install --no-cache-dir -r utils/requirements.txt
```

## Usage
After the installation process, you can start the 
program by running the following command :
```
python extractor.py
```
You have the choice between yake and bert for your
extraction task. 
Depending on which one you choose, you will have specific
parameters to provide.<br>
The program also allows you to generate a file with the
list of extracted keywords from text corpus.

## Author
Thierno Ibrahima Cisse
