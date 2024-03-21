import math


class Pair:
    def __init__(self, a: float, b: float):
        self.A = a  # Первый катет
        self.B = b  # Второй катет

    def change_numbers(self, a: float, b: float) -> None:
        """Метод для изменения значений катетов A и B."""
        self.A = a
        self.B = b

    def product(self) -> float:
        """Метод для вычисления произведения катетов A и B."""
        return self.A * self.B

    def sum(self) -> float:
        """Метод для вычисления суммы катетов A и B."""
        return self.A + self.B


class RightTriangle(Pair):
    def __init__(self, a: float, b: float):
        super().__init__(a, b)

    def hypotenuse(self) -> float:
        """Метод для вычисления длины первой гипотенузы прямоугольного треугольника."""
        return math.sqrt(self.A ** 2 + self.B ** 2)

    def second_hypotenuse(self) -> float:
        """Метод для вычисления длины второй гипотенузы прямоугольного треугольника."""
        return math.sqrt(self.A ** 2 + self.B ** 2 + (2 * self.A * self.B))

    def area(self) -> float:
        """Метод для вычисления площади прямоугольного треугольника."""
        return 0.5 * self.A * self.B


# Пример использования классов
pair1 = Pair(5, 8)
triangle1 = RightTriangle(pair1.A, pair1.B)

# Вывод информации о прямоугольном треугольнике
print("Гипотенуза △ABC:", "{:.2f}".format(triangle1.hypotenuse()))
print("Прямоугольный треугольник △ABC ({}, {}, {:.2f})".format(triangle1.A, triangle1.B, triangle1.hypotenuse()))
print("Площадь △ABC:", "{:.1f}".format(triangle1.area()))
print()
print("Сумма:", pair1.sum())
print("Произведение:", pair1.product())
print()

pair2 = Pair(15, 20)
triangle2 = RightTriangle(pair2.A, pair2.B)

# Вывод информации о прямоугольном треугольнике
print("Гипотенуза △ABC:", "{:.2f}".format(triangle2.hypotenuse()))
print("Гипотенуза △ABC:", "{:.2f}".format(triangle2.second_hypotenuse()))
print("Сумма:", pair2.sum())
print("Произведение:", pair2.product())
print("Площадь △ABC:", "{:.1f}".format(triangle2.area()))
print()
