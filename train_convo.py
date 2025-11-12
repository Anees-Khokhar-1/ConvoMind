import json
import numpy as np
import pickle
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import legacy
from tensorflow.keras.utils import to_categorical

# Import your helper functions
from utils.preprocess import tokenize, lemmatize, bag_of_words

# Load intents file
with open("data/intents.json", "r", encoding="utf-8") as f:
    intents = json.load(f)

words = []
classes = []
documents = []

# Loop through intents
for intent in intents['intents']:
    for pattern in intent['patterns']:
        w = tokenize(pattern)
        words.extend(w)
        documents.append((w, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# Lemmatize and sort words
words = [lemmatize(w.lower()) for w in words if w.isalpha()]
words = sorted(list(set(words)))
classes = sorted(list(set(classes)))

# Save words and classes
pickle.dump(words, open("models/words.pkl", "wb"))
pickle.dump(classes, open("models/classes.pkl", "wb"))

# Create training data
training = []
output_empty = [0] * len(classes)

for doc in documents:
    bag = bag_of_words(doc[0], words)
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1
    training.append([bag, output_row])

training = np.array(training, dtype=object)
train_x = np.array(list(training[:, 0]))
train_y = np.array(list(training[:, 1]))

# Build the model
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(64, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation="softmax"))

# Compile model using legacy SGD optimizer (for decay support)
sgd = legacy.SGD(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(optimizer=sgd, loss="categorical_crossentropy", metrics=["accuracy"])

# Train model
hist = model.fit(train_x, train_y, epochs=200, batch_size=5, verbose=1)

# Save model
model.save("models/chatbot_model.h5", hist)
print("✅ Model created and saved successfully!")
