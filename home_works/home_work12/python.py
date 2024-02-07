data = {
    "John": {
        "N": 3056,
        "S": 8463,
        "E": 8441,
        "W": 2694
    },
    "Tom": {
        "N": 4832,
        "S": 6786,
        "E": 4737,
        "W": 3612
    },
    "Anne": {
        "N": 5239,
        "S": 4802,
        "E": 5820,
        "W": 1859
    },
    "Fiona": {
        "N": 3904,
        "S": 3645,
        "E": 8821,
        "W": 2451
    }
}


for x in data:
    print(x)
    for y in data[x]:
        print("\t",  y, ":", data[x][y])


while True:
    person = input("Введите имя пользователя: ").capitalize()
    if person in data.keys():
        region = input("Выберите регион: ").upper()
        if region in data[person]:
            print(data[person][region])
            try:
                new_data = int(input("Введите новую дату: "))
                data[person][region] = new_data
                print(data[person])
                break
            except ValueError:
                print("Введите целочисленное число")
        else:
            print("Такого региона нет")
            break
    else:
        print("Пользователя с таким именем нету")
        break
