# В этот раз Вам нужно будет реализовать работу с исключениями, чтобы в крайних случаях, например,
# при попытке создания существующей заметки,
# или при попытке перевода ее в невалидное состояние (ни одно из ['ожидает', 'готово', 'в работе']),
# выбрасывалось исключение. Создать исключения нужно будет свои, и не забудьте, чтобы названия классов были говорящими,
# например, если не удается найти пользователя, то выбрасывается исключение UserNotFoundError.
# Эти исключения не нужно никак обрабатывать,
# этим будут заниматься другие сервисы, которые будут работать с Вашим NoteManager.
# Как и в прошлый раз, Вам нужно будет принимать некоторые решения самостоятельно, это поможет Вам в будущем, уже на
# на "боевых" проектах.


# РЕШЕНИЕ

import json


class Note:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def __repr__(self):
        return f"Note(name={self.name}, status={self.status})"


class NoteAlreadyExistsError(Exception):
    """Исключение, выбрасываемое при попытке создать уже существующую заметку."""
    pass


class UserNotFoundError(Exception):
    """Исключение, выбрасываемое, когда пользователь не найден."""
    pass


class InvalidNoteStatusError(Exception):
    """Исключение, выбрасываемое при попытке установить невалидный статус заметки."""
    pass


class NoteManager:
    def __init__(self):
        self.notes = {}

    def create_user(self, user_name):
        """Создает нового пользователя с указанным именем."""
        if user_name not in self.notes:
            self.notes[user_name] = {}
            return True
        return False

    def create_note(self, user_name, note_name, note_status):
        """Создает новую заметку для указанного пользователя."""
        if user_name not in self.notes:
            raise UserNotFoundError(f"Пользователь '{user_name}' не найден.")
        if note_status not in ['ожидает', 'готово', 'в работе']:
            raise InvalidNoteStatusError(f"Статус '{note_status}' является недопустимым.")
        if note_name in self.notes[user_name]:
            raise NoteAlreadyExistsError(f"Заметка '{note_name}' уже существует для пользователя '{user_name}'.")

        # Создаем заметку
        self.notes[user_name][note_name] = Note(note_name, note_status)
        return True

    def get_note(self, user_name, note_name):
        """Получает статус заметки указанного пользователя."""
        if user_name in self.notes and note_name in self.notes[user_name]:
            return self.notes[user_name][note_name]
        return None  # Возвращаем None, если пользователь или заметка не найдены

    def update_note(self, user_name, note_name, new_status):
        """Обновляет статус заметки указанного пользователя."""
        if (user_name not in self.notes
                or note_name not in self.notes[user_name]):
            raise UserNotFoundError(f"Пользователь '{user_name}' или заметка '{note_name}' не найдены.")

        if new_status not in ['ожидает', 'готово', 'в работе']:
            raise InvalidNoteStatusError(f"Статус '{new_status}' является недопустимым.")

        self.notes[user_name][note_name].status = new_status
        return True

    def delete_note(self, user_name, note_name):
        """Удаляет заметку указанного пользователя."""
        if user_name in self.notes and note_name in self.notes[user_name]:
            del self.notes[user_name][note_name]
            return True
        return None  # Возвращаем None, если пользователь или заметка не найдены

    def load_from_file(self, file_path):
        """Загружает заметки из файла."""
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for user_name, notes in data.items():
                self.create_user(user_name)
                for note_name, note_info in notes.items():
                    self.create_note(user_name, note_name, note_info['status'])

    def save_to_file(self, file_path):
        """Сохраняет заметки в файл."""
        with open(file_path, 'w', encoding='utf-8') as file:
            json_data = {user_name: {note_name: {'status': note.status} for note_name, note in notes.items()}
                         for user_name, notes in self.notes.items()}
            json.dump(json_data, file, ensure_ascii=False, indent=4)


# Пример использования
note_manager = NoteManager()

try:
    note_manager.create_user('new_user')
    note_manager.create_note('new_user', 'my_note', 'ожидает')
    print(note_manager.get_note('new_user', 'my_note'))  # Вывод: Note(name=my_note, status=ожидает)
    note_manager.update_note('new_user', 'my_note', 'готово')
    print(note_manager.get_note('new_user', 'my_note'))  # Вывод: Note(name=my_note, status=готово)
    note_manager.delete_note('new_user', 'my_note')
    print(note_manager.get_note('new_user', 'my_note'))  # Вывод: None
    note_manager.save_to_file('notes.json')  # Сохраняем заметки в файл
except (NoteAlreadyExistsError, UserNotFoundError, InvalidNoteStatusError) as e:
    print(f"Ошибка: {e}")
