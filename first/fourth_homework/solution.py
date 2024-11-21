titles = []

username = input("Введите имя пользователя: ")
content = input("Введите содержание заметки: ")
status = input("Введите статус заметки (например, 'В работе'): ")
created_date = input("Введите дату создания заметки (в формате дд-mm-yyyy): ")
issue_date = input("Введите дату истечения заметки (в формате дд-mm-yyyy): ")

# Запрос заголовков заметок
title1 = input("Введите заголовок первой заметки: ")
title2 = input("Введите заголовок второй заметки: ")
title3 = input("Введите заголовок третьей заметки: ")

# Добавление заголовков в список
titles.append(title1)
titles.append(title2)
titles.append(title3)

# Вывод информации о заметке
print("Имя пользователя:", username)
print("Заголовки:", titles)
print("Содержание:", content)
print("Статус:", status)
print("Дата создания:", created_date)
print("Дата истечения:", issue_date)
