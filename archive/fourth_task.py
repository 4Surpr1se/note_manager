# В этот раз Вам нужно будет разложить Ваши функции в отдельный модуль note_utils.py, импортировать их в файл main.py,
# где нужно будет продемонстрировать работу с заметками.
# Это позволит логически разделить Ваш проект на две части: часть работы со словарем и часть работы с самими функциями,
# чтобы в дальнейшем, в случае переписывания логики функций, исходный код main.py никак не менялся

# РЕШЕНИЕ

# note_utils.py
notes = {}


def create_user(user_name):
    """Создает нового пользователя с указанным именем."""
    if user_name not in notes:
        notes[user_name] = {}
        return True
    return False


def create_note(user_name, note_name, note_status):
    """Создает новую заметку для указанного пользователя."""
    if user_name not in notes:
        return None  # Возвращаем None, если пользователь не существует
    if note_status not in ['ожидает', 'готово', 'в работе']:
        return None
    if note_name in notes[user_name]:
        return None  # Возвращаем None, если заметка с таким именем уже существует
    # Создаем заметку
    notes[user_name][note_name] = note_status
    return True


def get_note(user_name, note_name):
    """Получает статус заметки указанного пользователя."""
    if user_name in notes and note_name in notes[user_name]:
        return notes[user_name][note_name]
    return None  # Возвращаем None, если пользователь или заметка не найдены


# main.py
from note_utils import create_user, create_note, get_note

create_user("Alice")
create_note("Alice", "Shopping List", "ожидает")
print(get_note("Alice", "Shopping List"))  # Вывод: ожидает
print(get_note("Alice", "Nonexistent Note"))  # Вывод: None
print(create_note("Bob", "Note for Bob", "Active"))  # Вывод: None (пользователь Bob не создан)
