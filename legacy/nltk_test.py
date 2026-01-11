import nltk
from nltk.tokenize import word_tokenize
from nltk.data import find
import os

# Manually set the NLTK data path to include both folders
nltk.data.path = [
    os.path.join(os.getenv('APPDATA'), 'nltk_data'),  # C:\Users\hp\AppData\Roaming\nltk_data
    os.path.join(os.getcwd(), 'nltk_data')            # D:\ConvoMind\nltk_data
]

print("Using NLTK data paths:", nltk.data.path)

# Verify punkt and wordnet availability
try:
    find('tokenizers/punkt')
    find('corpora/wordnet')
    find('tokenizers/punkt_tab')
    print("✅ Punkt, Punkt_tab, and WordNet found successfully!")
except LookupError as e:
    print("❌ Missing data:", e)

# Test tokenization
tokens = word_tokenize("Hello, this is a test of your local NLTK setup!")
print("Tokens:", tokens)
