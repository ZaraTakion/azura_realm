import json
import os

DATA_FOLDER = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data')

def load_json(filename: str):
    path = os.path.join(DATA_FOLDER, filename)
    with open(path, 'r', encoding='utf8') as f:
        return json.load(f)

def save_json(filename: str, data):
    path = os.path.join(DATA_FOLDER, filename)
    with open(path, 'w', encoding='utf8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
