from abc import ABC, abstractmethod
import math


class Shape(ABC):
    def __init__(self, color: str) -> None:
        """
        Инициализация фигуры.
        """
        self.color = color

    @abstractmethod
    def perimeter(self) -> float:
        """
        Вычисление периметра фигуры.
        """
        pass

    @abstractmethod
    def area(self) -> float:
        """
        Вычисление площади фигуры.
        """
        pass

    @abstractmethod
    def draw(self) -> None:
        """
        Отрисовка фигуры.
        """
        pass

    def display_info(self) -> None:
        """
        Вывод информации о фигуре.
        """
        print(f"=== {self.__class__.__name__} ===")
        self.additional_info()
        print(f"Цвет: {self.color}")
        print(f"Площадь: {self.area()}")
        print(f"Периметр: {self.perimeter()}")
        self.draw()
        print()

    @abstractmethod
    def additional_info(self) -> None:
        """
        Дополнительная информация о фигуре.
        """
        pass


class Square(Shape):
    def __init__(self, side_length: float, color: str) -> None:
        """
        Инициализация квадрата.
        """
        super().__init__(color)
        self.side_length = side_length

    def perimeter(self) -> float:
        return 4 * self.side_length

    def area(self) -> float:
        return self.side_length ** 2

    def draw(self) -> None:
        for _ in range(self.side_length):
            print("* " * self.side_length)

    def additional_info(self) -> None:
        print(f"Сторона: {self.side_length}")


class Rectangle(Shape):
    def __init__(self, length: float, width: float, color: str) -> None:
        """
        Инициализация прямоугольника.
        """
        super().__init__(color)
        self.length = length
        self.width = width

    def perimeter(self) -> float:
        return 2 * (self.length + self.width)

    def area(self) -> float:
        return self.length * self.width

    def draw(self) -> None:
        for _ in range(self.width):
            print("* " * self.length)

    def additional_info(self) -> None:
        print(f"Длина: {self.length}")
        print(f"Ширина: {self.width}")


class Triangle(Shape):
    def __init__(self, side1: float, side2: float, side3: float, color: str) -> None:
        """
        Инициализация треугольника.
        """
        super().__init__(color)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self) -> float:
        return round(self.side1 + self.side2 + self.side3, 1)

    def area(self) -> float:
        s = self.perimeter() / 2
        return round(math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3)), 2)

    def draw(self) -> None:
        height = max(self.side1, self.side2, self.side3)
        for i in range(1, height + 1):
            spaces = " " * (height - i)
            stars = "* " * i
            print(spaces + stars)

    def additional_info(self) -> None:
        print(f"Сторона 1: {self.side1}")
        print(f"Сторона 2: {self.side2}")
        print(f"Сторона 3: {self.side3}")


# Пример использования:

square = Square(3, "red")
rectangle = Rectangle(7, 3, "green")
triangle = Triangle(11, 6, 6, "yellow")

shapes = [square, rectangle, triangle]

for shape in shapes:
    shape.display_info()
