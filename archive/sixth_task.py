# В этот раз Вам нужно будет создать класс NoteManager, который будет осуществлять работу с заметами Note.
# Нужно будет перенести функции create_user, create_note и get_note в Класс NoteManager.
# Также нужно будет добавить методы update_note и delete_note, которые будут обновлять и удалять заметки пользователей
# Например note_manager_instance.get_note('my_user_name', 'my_note')
# Должен возвращать экземпляр класса Note с полями name и status,
# равными 'my_user_name' и 'my_note' соответственно,
# если у такого пользователя нет такой заметки или данный пользователь не существует, возвращает None
#

# РЕШЕНИЕ

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


# Пример использования
note_manager = NoteManager()
note_manager.create_user('my_user_name')
note_manager.create_note('my_user_name', 'my_note', 'ожидает')
print(note_manager.get_note('my_user_name', 'my_note'))  # Вывод: Note(name=my_note, status=ожидает)
note_manager.update_note('my_user_name', 'my_note', 'готово')
print(note_manager.get_note('my_user_name', 'my_note'))  # Вывод: Note(name=my_note, status=готово)
note_manager.delete_note('my_user_name', 'my_note')
print(note_manager.get_note('my_user_name', 'my_note'))  # Вывод: None