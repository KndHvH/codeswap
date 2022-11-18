import os
scriptPath = os.path.dirname(__file__)

def saveBody(body: str, title: str):
    relPath = 'database/'+title+'.txt'
    filepath = os.path.join(scriptPath, relPath)
    with open(filepath, "w") as file:
        file.write(body)


def getBody(key) -> str:
    try:
        relPath = 'database/'+key+'.txt'
        filepath = os.path.join(scriptPath, relPath)
        with open(filepath, "r") as file:
            body = file.read()
        return body

    except FileNotFoundError:
        return 'None'