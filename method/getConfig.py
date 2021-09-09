import json
def getJson(key):
    f = open('method/config.json')
    t = json.load(f)
    data = t.get(key)
    return data