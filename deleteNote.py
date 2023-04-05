from editNote import findKey


def delete(dict):
    for item in dict.values():
        print(
            f"Заголовок:{item['id']}\n Текст:{item['body']}\n Дата изменения:{item['change-date']}\t Дата создания:{item['creating-date']}\n")

    try:
        nameToDelete = "ID"+str(input("Введите id заметки на удаление: "))
        dict.pop(nameToDelete)
    except ValueError:
        print("Ошибка в исполнении удаления")
