from math import sqrt, pi

print("1 - прямоугольник,\n2 - треугольник,\n3 - круг")
figure = input("Выберите фигуру: ")

if figure == '1':
    a = float(input("Введите сторону a = "))
    b = float(input("Введите сторону b = "))
    print(f"Площадь =", a * b)
elif figure == '2':
    a = float(input("Введите сторону a = "))
    b = float(input("Введите сторону b = "))
    c = float(input("Введите сторону c = "))
    p = (a + b + c) / 2
    s = round(sqrt(p * (p - a) * (p - b) * (p - c)), 2)
    print(f"Площадь =", s)
elif figure == '3':
    r = float(input("Радиус круга R = "))
    print(f"Площадь:", round(pi * r ** 2, 2))
else:
    print("Ошибка ввода")
