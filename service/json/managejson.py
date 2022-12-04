import os
scriptPath = os.path.dirname(__file__)
import json

def save_json(dict):
    #{'code': [{'title': 'test', 'file': 'rfxr'}]}
    title = dict['code'][0]['title']
    relPath = '../../database/'+title+'.json'
    filepath = os.path.join(scriptPath, relPath)
    with open(filepath, 'w') as outfile:
        outfile.write(dict) if type(dict) == str else json.dump(dict, outfile)
        # remove str\


def read_json(title):
    try:
        relPath = '../../database/'+title+'.json'
        filepath = os.path.join(scriptPath, relPath)
        with open(filepath, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return 'None'   