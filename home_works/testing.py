import requests
import json
import csv

# Получаем данные о задачах с удаленного сервера
response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

# Определяем заголовки CSV файла
csv_columns = ['userId', 'id', 'title', 'completed']

# Открываем CSV файл для записи
with open('todos.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, delimiter=";", fieldnames=csv_columns)

    # Записываем заголовки
    writer.writeheader()

    # Записываем данные
    for todo in todos:
        writer.writerow(todo)