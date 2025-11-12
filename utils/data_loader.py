import json

def load_intents(file_path):
    """Load intents JSON file"""
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data['intents']
