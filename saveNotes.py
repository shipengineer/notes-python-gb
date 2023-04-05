import json


def saveAll(template, directory="./Python/app/storage.json"):
    with open(directory, "w", encoding="UTF-8") as storage:
        json.dump(template, storage, ensure_ascii=False)
