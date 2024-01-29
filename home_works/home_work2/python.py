num = int(input())
if 1 <= num <= 99:
    if num % 10 == 1 and num % 100 != 11:
        print(num, 'копейка')
    elif num % 10 in [2, 3, 4] and num % 100 not in [12, 13, 14]:
        print(num, 'копейки')
    else:
        print(num, 'копеек')
else:
    print("Ошибка ввода данных")

