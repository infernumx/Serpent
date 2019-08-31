import rapidjson

def json_load(filename):
	with open(filename) as f:
		return rapidjson.loads(f.read())