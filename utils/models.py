"""
models
-----
Functions for extracting keywords.
Contents:
    yake_extractor,
    bert_extractor,
"""
import yake
from kwx.model import extract_kws

# Creating custom stoplist from stopwords.txt
stop_list = []
with open('utils/stopwords.txt', 'r') as f:
    for line in f:
        stop_list.append(line.strip())
    f.close()


def yake_extractor(text, topn, ngram):
    """
        Load a corpus and extract the specified number of keywords
        Parameters
        ----------
            text : str
                Data extracted and merged from dita files
            ngram : int
                Length of a single keywords (default=1)
            topn : int
                Number of keyword extracted (default=10)
        Returns
        -------
            keywords_list : list
                List of extracted keywords
    """
    if ngram is None:
        ngram = 1
    if topn is None:
        topn = 10
    kw_extractor = yake.KeywordExtractor(top=topn, n=ngram, stopwords=stop_list)
    return kw_extractor.extract_keywords(text)


def bert_extractor(text, top_keywords, ntopics):
    """
        Load a corpus and extract the specified number of keywords
        Parameters
        ----------
            text : str
                Data extracted and merged from dita files
            top_keywords : int
                Length of a single keywords (default=1)
            ntopics : int
                The number of categories for BERT (default=10)
        Returns
        -------
            keywords_list : list
                List of extracted keywords
    """
    input_language = "english"
    if top_keywords is None:
        top_keywords = 10
    if ntopics is None:
        ntopics = 5
    return extract_kws(
        method="BERT",
        text_corpus=text,
        input_language=input_language,
        num_keywords=top_keywords,
        num_topics=ntopics,
        prompt_remove_words=False,
        show_progress_bar=False,
        batch_size=32,
    )
