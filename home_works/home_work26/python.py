class Student:
    """Класс, представляющий студента."""

    def __init__(self, name: str, laptop: 'Laptop'):
        """Инициализирует объект студента."""
        self.name = name
        self.laptop = laptop

    def __str__(self) -> str:
        """Возвращает строковое представление объекта студента."""
        return f"{self.name} => {self.laptop.model}, {self.laptop.processor}, {self.laptop.memory}"

    class Laptop:
        """Класс, представляющий ноутбук."""

        def __init__(self, model: str, processor: str, memory: int):
            """Инициализирует объект ноутбука."""
            self.model = model
            self.processor = processor
            self.memory = memory


laptop1 = Student.Laptop("HP", "i7", 16)
student1 = Student("Roman", laptop1)

laptop2 = Student.Laptop("HP", "i7", 16)
student2 = Student("Vladimir", laptop2)

print(student1)
print(student2)
