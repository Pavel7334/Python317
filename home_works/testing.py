import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

# Функция для проверки, является ли задача завершенной
def is_completed(todo):
    return todo["completed"]

# Словарь для хранения задач для каждого пользователя
user_tasks = {"userId_5": [], "userId_10": []}

# Добавление завершенных задач для userId 5 и userId 10 в словарь
for todo in todos:
    if todo["userId"] == 5 and is_completed(todo):
        user_tasks["userId_5"].append(todo)
    elif todo["userId"] == 10 and is_completed(todo):
        user_tasks["userId_10"].append(todo)

# Запись в JSON-файл
with open("user_tasks.json", "w") as json_file:
    json.dump(user_tasks, json_file, indent=4)

print("Завершенные задачи для пользователей с userId 5 и userId 10 были сохранены в файл 'user_tasks.json'.")
