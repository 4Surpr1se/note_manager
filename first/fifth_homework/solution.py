note = {}

note['titles'] = []

note['username'] = input("Введите имя пользователя: ")
note['content'] = input("Введите содержание заметки: ")
note['status'] = input("Введите статус заметки (например, 'В работе'): ")
note['created_date'] = input("Введите дату создания заметки (в формате дд-мм-гггг): ")
note['issue_date'] = input("Введите дату истечения заметки (в формате дд-мм-гггг): ")

# Запрос заголовков заметок
title1 = input("Введите заголовок первой заметки: ")
title2 = input("Введите заголовок второй заметки: ")
title3 = input("Введите заголовок третьей заметки: ")

# Добавление заголовков в список
note['titles'].append(title1)
note['titles'].append(title2)
note['titles'].append(title3)

# Вывод информации о заметке
print("Имя пользователя:", note['username'])
print("Заголовки:", note['titles'])
print("Содержание:", note['content'])
print("Статус:", note['status'])
print("Дата создания:", note['created_date'])
print("Дата истечения:", note['issue_date'])