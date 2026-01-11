import os
import random
import pickle
import numpy as np
from tensorflow.keras.models import load_model
from utils.data_loader import load_intents
from utils.response_selector import get_response

# ----------------------------
# Memory-friendly lemmatizer
# ----------------------------
def lemmatize(word):
    """
    Simple lemmatization: lowercase only.
    This avoids loading NLTK WordNet and memory errors.
    """
    return word.lower()

# ----------------------------
# Tokenization + bag of words
# ----------------------------
def tokenize(sentence):
    """
    Simple whitespace tokenizer.
    """
    return sentence.strip().split()

def bag_of_words(tokenized_sentence, words):
    """
    Create a bag-of-words vector.
    """
    sentence_words = [lemmatize(word) for word in tokenized_sentence]
    bag = [1 if w in sentence_words else 0 for w in words]
    return np.array(bag)

# ----------------------------
# Paths
# ----------------------------
MODEL_PATH = 'models/chatbot_model.h5'
WORDS_PATH = 'models/words.pkl'
CLASSES_PATH = 'models/classes.pkl'
INTENTS_PATH = 'data/intents.json'

# ----------------------------
# Load model and data
# ----------------------------
print("Loading model and data...")
model = load_model(MODEL_PATH)
words = pickle.load(open(WORDS_PATH, 'rb'))
classes = pickle.load(open(CLASSES_PATH, 'rb'))
intents = load_intents(INTENTS_PATH)
print("✅ ConvoMind is ready!")

# ----------------------------
# Predict intent
# ----------------------------
def predict_class(sentence):
    bow = bag_of_words(tokenize(sentence), words)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return [{"intent": classes[r[0]], "probability": str(r[1])} for r in results]

# ----------------------------
# Chat loop
# ----------------------------
def chat():
    print("\nConvoMind is online! Type 'quit' to exit.")
    while True:
        message = input("You: ")
        if message.lower() == 'quit':
            print("ConvoMind: Goodbye!")
            break

        intents_list = predict_class(message)
        if intents_list:
            response = get_response(intents_list, intents)
            print(f"ConvoMind: {response}")
        else:
            print("ConvoMind: I don't understand, can you rephrase?")

# ----------------------------
# Run chatbot
# ----------------------------
if __name__ == "__main__":
    chat()
