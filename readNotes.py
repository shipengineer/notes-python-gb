import json


def read(directory="./Python/app/storage.json"):
    with open(directory) as storage:
        templates = json.load(storage)
        # print(templates)
        return templates



