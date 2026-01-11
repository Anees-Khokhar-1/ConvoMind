import nltk
import os

# Set NLTK data download directory (optional)
nltk_data_dir = os.path.join(os.getenv('APPDATA'), 'nltk_data')

# Ensure the directory exists
os.makedirs(nltk_data_dir, exist_ok=True)

# Download necessary NLTK packages
nltk.download("punkt", download_dir=nltk_data_dir)
nltk.download("wordnet", download_dir=nltk_data_dir)
nltk.download("omw-1.4", download_dir=nltk_data_dir)

print("✅ NLTK data (Punkt, WordNet, OMW) downloaded successfully!")


