class IntegerCoordinate:
    """
    Дескриптор для проверки целочисленных значений координат.
    """

    def __init__(self, name: str) -> None:
        self.name = name

    def __get__(self, instance: 'Point3D', owner: type) -> int:
        return instance.__dict__[self.name]

    def __set__(self, instance: 'Point3D', value: int) -> None:
        if not isinstance(value, int):
            raise ValueError("Значение координаты должно быть целым числом")
        instance.__dict__[self.name] = value


class Point3D:
    """
    Класс для представления точки в трехмерном пространстве.
    """

    def __init__(self, x: int, y: int, z: int) -> None:
        """
        Инициализация точки в трехмерном пространстве.
        """
        self._x: int = IntegerCoordinate('_x')
        self._y: int = IntegerCoordinate('_y')
        self._z: int = IntegerCoordinate('_z')

        self._x = x
        self._y = y
        self._z = z

    def __repr__(self) -> str:
        """
        Возвращает строковое представление точки.
        """
        return f"{{'_x': {self._x}, '_y': {self._y}, '_z': {self._z}}}"


point = Point3D(1, 2, 3)
print(point)
