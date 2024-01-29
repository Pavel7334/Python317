s = []
for num in range(int(input("Кол-во элементов списка: "))):
    x = int(input("Введите число кратное 3: "))
    if x % 3 != 0:
        print(f"{x} не делится на 3 без остатка")
    else:
        s.append(x)
print(s)