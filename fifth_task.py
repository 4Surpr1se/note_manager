# Переделайте Ваш код таким образом, чтобы каждая заметка была экземпляром класса Note.
# Каждый экземпляр должен иметь поля user_name, note_name, note_status.
# Функции create_user, create_note, get_note иметь тот же функционал и работать корректно с новой структурой.

# РЕШЕНИЕ

class Note:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def __repr__(self):
        return f"Note(name={self.name}, status={self.status})"


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
    notes[user_name][note_name] = Note(note_name, note_status)
    return True


def get_note(user_name, note_name):
    """Получает статус заметки указанного пользователя."""
    if user_name in notes and note_name in notes[user_name]:
        return notes[user_name][note_name]
    return None  # Возвращаем None, если пользователь или заметка не найдены
