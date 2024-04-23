import requests
import json
import csv
from typing import List, Dict


def fetch_todos(url: str) -> List[Dict]:
    """
    Получает данные о задачах с удаленного сервера и возвращает их в виде списка словарей.

    Parameters:
        url (str): URL-адрес для запроса данных о задачах.

    Returns:
        List[Dict]: Список словарей с данными о задачах.
    """
    response = requests.get(url)
    todos = json.loads(response.text)
    return todos


def write_todos_to_csv(todos: List[Dict], filename: str) -> None:
    """
    Записывает список словарей в файл CSV.

    Parameters:
        todos (List[Dict]): Список словарей с данными о задачах.
        filename (str): Имя файла, в который будут записаны данные.

    Returns:
        None
    """
    # Определяем заголовки CSV файла
    csv_columns = ['userId', 'id', 'title', 'completed']

    # Открываем CSV файл для записи
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, delimiter=";", fieldnames=csv_columns)

        # Записываем заголовки
        writer.writeheader()

        # Записываем данные
        for todo in todos:
            writer.writerow(todo)


# Получаем данные о задачах с удаленного сервера
todos_url = "https://jsonplaceholder.typicode.com/todos"
todos_data = fetch_todos(todos_url)

# Записываем данные в CSV файл
csv_filename = "todos.csv"
write_todos_to_csv(todos_data, csv_filename)

#                                           Версия 2.0

# import requests
# import json
# import csv
#
# # Получаем данные о задачах с удаленного сервера
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# todos = json.loads(response.text)
#
# # Определяем заголовки CSV файла
# csv_columns = ['userId', 'id', 'title', 'completed']
#
# # Открываем CSV файл для записи
# with open('todos.csv', 'w', newline='') as csvfile:
#     writer = csv.DictWriter(csvfile, delimiter=";", fieldnames=csv_columns)
#
#     # Записываем заголовки
#     writer.writeheader()
#
#     # Записываем данные
#     for todo in todos:
#         writer.writerow(todo)

