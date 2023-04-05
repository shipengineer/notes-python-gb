from datetime import datetime
import random


def create(template):
    now = datetime.now()
    ID = random.randint(1, 5000)
    while (ID in template.keys()):
        ID = random.randint(1, 5000)

    newNote = {f"{ID}": {"name": "", "body": "",
                         "creating-date": "", "change-date": ""}}
    newNote[f"{ID}"]["name"] = input("Введите заголовок заметки: ")
    newNote[f"{ID}"]["body"] = input("Текст заметки: ")
    newNote[f"{ID}"]["creating-date"] = now.strftime("%d/%m/%Y %H:%M:%S")
    newNote[f"{ID}"]["change-date"] = now.strftime("%d/%m/%Y %H:%M:%S")
    template[f"{ID}"] = newNote[f"{ID}"]



