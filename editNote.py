

temp = {
    "ID2164": {
        "id": "ID2164",
        "name": "третья",
        "body": "sssss",
        "creating-date": "05/04/2023 16:04:37",
        "change-date": "05/04/2023 16:04:37"
    },
    "ID774": {
        "id": "ID774",
        "name": "erwerw",
        "body": "sdfsdfv",
        "creating-date": "05/04/2023 16:04:46",
        "change-date": "05/04/2023 16:04:46"
    },
    "ID3998": {
        "id": "ID3998",
        "name": "третья",
        "body": "тело третьей",
        "creating-date": "05/04/2023 16:04:53",
        "change-date": "05/04/2023 16:04:53"
    }
}


def findKey(dict, value):
    # print(list(dict.items())[1])
    result = []
    for n in list(dict.items()):
        if (n[1]["name"] == value):
            result.append(n[1]["id"])
    return list(result)


def editOne(dict, ID):
    try:
        whatToChange = int(input(
            "Что нужно изменить:\n1-Заголовок заметки,\n2-Текст заметкиб\n3-удалить заметку\n"))
        match whatToChange:
            case 1:
                dict[f"{ID}"]["name"] = input("Введите новое имя: ")
            case 2:
                dict[f"{ID}"]["body"] = input("Введите новый текст: ")
            case 3:
                try:
                    dict.pop(ID)
                except ValueError:
                    print("Ошибка в исполнении удаления")
    except ValueError:
        print("Неверная команда, повторите ввод")


def edit(template, name):
    ID = findKey(template, name)
    if (len(ID) == 0):
        print("Заметок с таким именем нет")
    if (len(ID) > 1):
        print("Есть несколько заметок с таким заголовком\n")
        for item in template.values():
            print(
                f"Заголовок:{item['id']}\n Текст:{item['body']}\n Дата изменения:{item['change-date']}\t Дата создания:{item['creating-date']}\n")
        try:
            neededId = int(input("Укажите цифры id записи для изменения: "))
            print('ID'+str(neededId))
            editOne(template, 'ID'+str(neededId))
        except ValueError:
            print("Неверный id, повторите ввод")
    if (len(ID) == 1):

        editOne(template, ID[0])
