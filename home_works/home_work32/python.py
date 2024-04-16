import requests
import json

# Получаем данные о задачах с удаленного сервера
response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

# Словарь для хранения количества завершенных задач для каждого пользователя
todos_by_user = {}

# Подсчитываем количество завершенных задач для каждого пользователя
for todo in todos:
    if todo["completed"]:
        try:
            todos_by_user[todo["userId"]] += 1
        except KeyError:
            todos_by_user[todo["userId"]] = 1

# Сортируем словарь по количеству завершенных задач в обратном порядке
top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)

# Определяем максимальное количество завершенных задач
max_complete = top_users[0][1]

# Список для хранения пользователей с максимальным количеством завершенных задач
users = []

# Определяем пользователей с максимальным количеством завершенных задач
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(user)

# Словарь для хранения завершенных задач для каждого пользователя с userId 5 и userId 10
user_tasks = {"userId_5": [], "userId_10": []}


# Функция для проверки, является ли задача завершенной
def is_completed(todo):
    return todo["completed"]


# Добавляем завершенные задачи для userId 5 и userId 10 в соответствующие списки в словаре
for todo in todos:
    if todo["userId"] == 5 and is_completed(todo):
        user_tasks["userId_5"].append(todo)
    elif todo["userId"] == 10 and is_completed(todo):
        user_tasks["userId_10"].append(todo)

# Записываем данные о завершенных задачах пользователей в JSON-файл
with open("user_tasks.json", "w") as json_file:
    json.dump(user_tasks, json_file, indent=4)

# Формируем строку с информацией о пользователях с максимальным количеством завершенных задач
max_users = " and ".join([str(user) for user in users])

# Выводим сообщение о пользователях с максимальным количеством завершенных задач
print(f"Пользователи {max_users} завершили {max_complete} задач(и)")

# Выводим сообщение об успешном сохранении данных в JSON-файл
print("Завершенные задачи для пользователей с userId 5 и userId 10 были сохранены в файл 'user_tasks.json'.")
