from geometry import sqrt, pi


def rectangle(a: float, b: float) -> str:
    return f"Площадь прямоугольника: {a * b:.2f}"


def triangle(a: float, b: float, c: float) -> str:
    p = (a + b + c) / 2
    s = sqrt(p * (p - a) * (p - b) * (p - c))
    return f"Площадь треугольника: {s:.2f}"


def circle(r: float) -> str:
    return f"Площадь круга: {pi * r ** 2:.2f}"


enter_side = "Введите сторону"

side_a = f"{enter_side} a = "
side_b = f"{enter_side} b = "
side_c = f"{enter_side} c = "


print("1 - прямоугольник, 2 - треугольник, 3 - круг")
figure = input("Выберите фигуру: ")

if figure == '1':
    print(rectangle(float(input(side_a)), float(input(side_b))))
elif figure == '2':
    print(triangle(float(input(side_a)), float(input(side_b)), float(input(side_c))))
elif figure == '3':
    print(circle(float(input("Радиус круга R = "))))
else:
    print("Ошибка ввода")


