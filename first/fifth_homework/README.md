## Описание задачи

Ваша задача — улучшить структуру хранения данных заметки, используя словарь. Это позволит организовать информацию более
эффективно и удобно. Вместо создания отдельных переменных для каждого элемента заметки вы будете использовать один
словарь, который будет содержать все необходимые данные, включая заголовки заметок.

Преимущества использования словарей:
Организация данных: Все связанные данные хранятся в одном месте, что делает код более структурированным.
Удобство доступа: Доступ к данным осуществляется по ключам, что упрощает чтение и изменение значений.
Легкость расширения: Легко добавлять новые поля, просто добавляя новые ключи в словарь.
Упрощение передачи данных: Словари удобно передавать в функции или возвращать из них.
Читаемость: Код становится более понятным, так как все данные находятся в одном месте.

Шаги выполнения:

1) Создайте словарь для хранения информации о заметке.
2) Соберите данные от пользователя: имя, содержание, статус, даты и заголовки.
3) Добавьте заголовки в список внутри словаря.
4) Выведите собранные данные на экран.

В результате мы получим единый формат хранения заметок, что значительно упростит работу с ними, особенно когда их станет
много. Например, мы сможем передавать заметки в функции и хранить несколько из них в одном списке. Если бы мы
использовали обычные переменные для хранения информации о каждой заметке, это было бы затруднительно.

## Формат сдачи задания

Добавьте в Ваш репозиторий note_manager файл final.py,
который и будет содержать решение задачи

## **_`РЕШЕНИЕ`_**

```py
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

```