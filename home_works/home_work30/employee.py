class Employee:
    """Базовый класс для всех сотрудников"""

    def __init__(self, kod: int, name: str):
        self.id: int = kod
        self.name: str = name
