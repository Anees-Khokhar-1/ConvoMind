# utils/preprocess.py

import re
import numpy as np

# ----------------------------
# Simple "lemmatizer"
# ----------------------------
def lemmatize(word):
    """
    Memory-safe lemmatizer: just lowercase.
    Avoids NLTK WordNet to prevent MemoryError.
    """
    return word.lower()

# ----------------------------
# Tokenizer
# ----------------------------
def tokenize(sentence):
    """
    Tokenize the sentence by splitting on whitespace and punctuation.
    """
    sentence = re.sub(r'[^\w\s]', '', sentence)  # remove punctuation
    tokens = sentence.strip().split()
    return tokens

# ----------------------------
# Bag of words
# ----------------------------
def bag_of_words(tokenized_sentence, words):
    """
    Convert tokenized sentence to bag-of-words array.
    """
    sentence_words = [lemmatize(word) for word in tokenized_sentence]
    bag = [1 if w in sentence_words else 0 for w in words]
    return np.array(bag)
