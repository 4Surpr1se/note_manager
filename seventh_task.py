# В этот раз Вам нужно будет добавить загрузку в файл и из файла, чтобы Ваши заметки могли сохраняться
# после конца работы программы, и Вы бы могли использовать ранее сохраненные заметки, в качестве формата для хранения
# советуем использовать JSON,
# который поддерживает те же основные структуры данных,
# что и python (Тут Вам понадобятся два метода из библиотеки json: json.load(file)
# и json.dump(json_data, file, ensure_ascii=False), позволяющие загружать и сохранять данные соответственно).
# Однако, как и до этого мы не ограничиваем Вам в выборе, и если Вам кажется, что тут подойдет обычный txt
# или любой другой формат, то можете его смело реализовывать :)


# РЕШЕНИЕ

import json


class Note:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def __repr__(self):
        return f"Note(name={self.name}, status={self.status})"


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
            return None  # Возвращаем None, если пользователь не существует
        if note_status not in ['ожидает', 'готово', 'в работе']:
            return None
        if note_name in self.notes[user_name]:
            return None  # Возвращаем None, если заметка с таким именем уже существует
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
        if user_name in self.notes and note_name in self.notes[user_name]:
            if new_status in ['ожидает', 'готово', 'в работе']:
                self.notes[user_name][note_name].status = new_status
                return True
        return None  # Возвращаем None, если пользователь или заметка не найдены или статус некорректен

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
note_manager.load_from_file('notes.json')  # Загружаем заметки из файла
note_manager.create_user('new_user')
note_manager.create_note('new_user', 'my_note', 'ожидает')
print(note_manager.get_note('my_user_name', 'my_note'))  # Вывод: Note(name=my_note, status=ожидает)
note_manager.update_note('my_user_name', 'my_note', 'готово')
print(note_manager.get_note('my_user_name', 'my_note'))  # Вывод: Note(name=my_note, status=готово)
print(note_manager.get_note('my_user_name', 'my_note'))  # Вывод: None
note_manager.save_to_file('notes.json')  # Сохраняем заметки в файл
