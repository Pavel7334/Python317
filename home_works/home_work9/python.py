numbers = '0123456789'
tpl = tuple(input("Введите по порядку, без пробелов, элементы кортежа: "))
print(tpl)
for number in numbers:
    count = tpl.count(number)
    if count:
        print(f"Количество {number} = {count}")

