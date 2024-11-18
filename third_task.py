# В этот раз Вам нужно будет доработать Ваши предыдущие функции таким образом, чтобы программа запоминала,
# к какому пользователю привязана та или иная заметка, также Вам понадобится создать функцию create_user(user_name),
# При попытке создать заметку к несозданному пользователю, функция должна возвращать None.
#
# Теперь функции принимают следующие аргументы def create_note(user_name, note_name, note_status)
# и def get_note(user_name, note_name).
#
# Вы можете использовать дополнительные словари и структуры данных в случае необходимости,
# однако это задачу можно решить с помощью словарей, вложенных в один изначальный словарь.
#
# Как и в прошлый раз, поведение функций в крайних случаях оставляем на Ваше усмотрение.


# РЕШЕНИЕ

# Словарь для хранения пользователей и их заметок

users_notes = {}


def create_user(user_name):
    """Создает нового пользователя с указанным именем."""
    if user_name not in users_notes:
        users_notes[user_name] = {}
        return True
    return False


def create_note(user_name, note_name, note_status):
    """Создает новую заметку для указанного пользователя."""
    if user_name not in users_notes:
        return None  # Возвращаем None, если пользователь не существует
    if note_status not in ['ожидает', 'готово', 'в работе']:
        return None
    if note_name in users_notes[user_name]:
        return None  # Возвращаем None, если заметка с таким именем уже существует
    users_notes[user_name][note_name] = note_status
    return True


def get_note(user_name, note_name):
    """Получает статус заметки указанного пользователя."""
    if user_name in users_notes and note_name in users_notes[user_name]:
        return users_notes[user_name][note_name]
    return None  # Возвращаем None, если пользователь или заметка не найдены


# Пример использования
create_user("Alice")
create_note("Alice", "Shopping List", "ожидает")
print(get_note("Alice", "Shopping List"))  # Вывод: ожидает
print(get_note("Alice", "Nonexistent Note"))  # Вывод: None
print(create_note("Bob", "Note for Bob", "Active"))  # Вывод: None (пользователь Bob не создан)
