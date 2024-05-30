import json
from keras.models import model_from_json

def load_model_from_json(json_path):
    with open(json_path, 'r') as json_file:
        model_json = json_file.read()
    model = model_from_json(model_json)
    return model

model = load_model_from_json('model.json')
