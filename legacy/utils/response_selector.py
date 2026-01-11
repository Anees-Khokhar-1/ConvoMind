import random

def get_response(intents_list, intents_json):
    """
    intents_list: model output list, e.g., [{'intent':'greeting', 'probability':0.99}]
    intents_json: loaded intents.json
    """
    tag = intents_list[0]['intent']
    for intent in intents_json:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])