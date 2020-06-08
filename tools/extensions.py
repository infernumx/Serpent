import json


def load_json(filename):
    with open(filename) as f:
        return json.loads(f.read())
