import os
scriptPath = os.path.dirname(__file__)

def titleVerif(title: str) -> bool:
    try:
        relPath = 'database/'+title+'.txt'
        filepath = os.path.join(scriptPath, relPath)
        with open(filepath, "r") as file:
            body = file.read()
        return False
    
    except FileNotFoundError:
        return True