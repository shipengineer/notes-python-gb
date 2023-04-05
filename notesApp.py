import json
import saveNotes
import readNotes
import editNote
import createNote


def app():
    template = readNotes.read()
    exectution = True
    while (exectution):
        template["wally"] = ['wallhack']
        print(template["wally"][0])
        # saveNotes.saveAll(template)
        exectution = False


app()
