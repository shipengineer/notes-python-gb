import json
import saveNotes
import readNotes
import editNote
import createNote


def app():
    template = readNotes.read()
    exectution = True
    while (exectution):
        createNote.create(template)
        saveNotes.saveAll(template)
        exectution = False


app()
