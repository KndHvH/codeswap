from service.swap import swap
import tkinter as tk
import os
scriptPath = os.path.dirname(__file__)


def saveBody(body, path, password):
    text = body.get(1.0, tk.END)

    text = swap(text, password)

    relPath = '../database/'+path+'.txt'
    filepath = os.path.join(scriptPath, relPath)
    with open(filepath, "w") as output_file:

        output_file.write(text)


def getBody(path) -> str:
    try:
        relPath = '../database/'+path+'.txt'
        filepath = os.path.join(scriptPath, relPath)
        with open(filepath, "r") as file:
            body = file.read()
        return body

    except FileNotFoundError:
        return '_insert here'
