from tkinter import *
from service.manageText import saveBody, getBody
from service.swap import swap


def textEditor(filepath, password):

    currentText = getBody(filepath)

    if currentText != '_insert here':
        currentText = swap(currentText, password)

    stimulator_window = Tk()
    stimulator_window.geometry('600x600')
    stimulator_window.title('_codeswap')

    scrollbar = Scrollbar(stimulator_window)
    scrollbar.pack(side=RIGHT, fill=Y)
    body = Text(stimulator_window, width=400, height=450,
                yscrollcommand=scrollbar.set)
    body.insert("1.0", currentText)
    body.pack(fill=BOTH)

    scrollbar.config(command=body.yview)

    button = Button(stimulator_window, text='Save', font=(
        'normal', 10), command=saveBody(body, filepath, password), bg='green')
    button.place(x=270, y=520)

    stimulator_window.mainloop()
