import json
import saveNotes
import readNotes
import editNote
import createNote
import deleteNote


def app():
    template = readNotes.read()
    exectution = True
    print("Добрый день!\n")

    while (exectution):
        try:
            print("___________________________________________________________________")
            command = int(input(
                "Введите команду\n1-Посмотреть записи\n2-Создать запись\n3-Редактировать запись\n4-Удалить запись\n5-Сохранить базу\n6-Выход\n___________________________________________________________________\nКоманда:"))

            match command:
                case 1:
                    readNotes.printNotes(template)
                case 2:
                    createNote.create(template)
                case 3:
                    nameToEdit = input(
                        "Укажите заголовок редактируемой заметки: ")
                    editNote.edit(template, nameToEdit)
                case 4:
                    deleteNote.delete(template)
                case 5:
                    saveNotes.saveAll(template)
                case 6:
                    qSave = input(
                        "Сохранить базу перед выходом Да/Нет любая кнопка для отмены\n")
                    match qSave:
                        case "Да":
                            saveNotes.saveAll(template)
                            exectution = False
                        case "Нет":
                            exectution = False
        except ValueError:
            print("Неверная команда, повторите ввод")
            print("___________________________________________________________________")


app()
