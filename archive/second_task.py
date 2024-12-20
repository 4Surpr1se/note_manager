# Вам нужно будет создать две функции: по созданию заметки в словаре и по получению статуса заметки по названию.
# Функция создания принимает название и статус заметки: def create_note(note_name, note_status)
# и запоминает соответствующие название и статус с помощью словаря notes, также Вам понадобится добавить проверку на то,
# что note_status соответствует одному из значений 'ожидает', 'готово' или 'в работе'.
# Функция получения принимает название заметки: def get_note(note_name)
# и возвращает соответствующий статус с помощью словаря notes.
#
# Поведение функций в крайних случаях, например,
# при отсутствии заметки в словаре при попытке ее получить,
# или неправильный note_status при создании, оставляем на Ваше усмотрение


# РЕШЕНИЕ
notes = {}


def create_note(note_name, note_status):
    if note_status in ['ожидает', 'готово', 'в работе']:
        notes[note_name] = note_status
    else:
        return 'wrong status'


def get_note(note_name):
    return notes.get(note_name)


create_note('покушать', 'в работе')
if get_note('покушать') == 'в работе':
    create_note('покушать', 'готово')
assert get_note('покушать') == 'готово'
