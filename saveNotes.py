import json


def saveOneNotes(noteToSave, directory="/Python/app/storage.json"):
    with open(directory) as storage:
        storage.write(json.dumps(noteToSave))


def saveAll(template, directory="./Python/app/storage.json"):
    with open(directory, "w", encoding="UTF-8") as storage:
        json.dump(template, storage, ensure_ascii=False)
