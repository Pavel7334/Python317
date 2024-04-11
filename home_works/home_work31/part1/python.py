import json
from random import choice


def gen_person() -> dict:
    """
    Генерирует случайное имя и номер телефона для человека.
    """
    name = ''
    tel = ''

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name) != 7:
        name += choice(letters)

    while len(tel) != 10:
        tel += choice(nums)

    person = {
        'name': name,
        'tel': tel
    }

    return person


def write_json(person_dict) -> None:
    """
    Записывает информацию о человеке в файл 'persons.json'.
    """
    try:
        with open('persons.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    if isinstance(data, list):
        data = {}

    next_index = max(map(int, data.keys()), default=0) + 1
    data[str(next_index)] = person_dict

    with open("persons.json", "w") as f:
        json.dump(data, f, indent=2)


for i in range(5):
    write_json(gen_person())
