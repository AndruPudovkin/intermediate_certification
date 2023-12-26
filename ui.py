import Note


def create_note():
    title = input('Введите Название заметки: ')
    body =  input('Введите Описание заметки: ')
    return Note.Note(title=title, body=body)


def menu():
    print("\nФункции:\n\n1 - вывод всех заметок из файла\n2 - добавление заметки\n3 - удаление заметки\n4 - редактирование заметки\n7 - выход\n\nВведите номер функции: ")


# def check_len_text_input(text, n):
#     while len(text) <= n:
#         print(f'Текст должен быть больше {n} символов\n')
#         text = input('Введите тескт: ')
#     else:
#         return text


def goodbuy():
    print("Конец")