import nltk
import os

# Choose a folder where memory issues are less likely
nltk_data_dir = os.path.join(os.getcwd(), 'nltk_data')

# Create folder if it doesn't exist
os.makedirs(nltk_data_dir, exist_ok=True)

# Download WordNet and OMW uncompressed
nltk.download('wordnet', download_dir=nltk_data_dir)
nltk.download('omw-1.4', download_dir=nltk_data_dir)

# Add this folder to NLTK's data path
nltk.data.path.append(nltk_data_dir)

print("✅ WordNet and OMW downloaded successfully!")
