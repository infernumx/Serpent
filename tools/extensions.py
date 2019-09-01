import rapidjson


def load_json(filename):
    with open(filename) as f:
        return rapidjson.loads(f.read())
