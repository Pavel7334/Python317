class Person:
    """Класс, представляющий человека с именем и возрастом."""

    def __init__(self, name: str, age: float) -> None:
        self.__name = name
        self.__age = age

    @staticmethod
    def __check_value(value, types) -> bool:
        return isinstance(value, types)

    @property
    def age(self) -> float:
        return self.__age

    @age.setter
    def age(self, value: float) -> None:
        if self.__check_value(value, (int, float)):
            self.__age = value

    @age.deleter
    def age(self) -> None:
        del self.__age

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if self.__check_value(value, str):
            self.__name = value

    @name.deleter
    def name(self) -> None:
        del self.__name


pers1 = Person("Irina", 26)
print(pers1.__dict__)
pers1.name = "Igor"
pers1.age = 31
print(pers1.name)
print(pers1.age)
pers1.age = 26
del pers1.name
print(pers1.__dict__)
