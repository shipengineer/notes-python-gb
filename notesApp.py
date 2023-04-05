import json


def function(x, y):
    return x+y


print(function(1, 2))


def app():
    exectution = False
    with open("./Python/app/storage.json") as storage:
        templates = json.load(storage)

        print(templates)
    for section, commands in templates.items():
        print(section)
        print('\n'.join(commands))


app()
