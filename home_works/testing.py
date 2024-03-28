class Student:

    def __init__(self, name, laptop):
        self.name = name
        self.laptop = laptop

    def __str__(self):
        return f"{self.name} => {self.laptop.model}, {self.laptop.processor}, {self.laptop.memory}"

    class Laptop:
        def __init__(self, model, processor, memory):
            self.model = model
            self.processor = processor
            self.memory = memory


laptop1 = Student.Laptop("HP", "i7", 16)
student = Student("Roman", laptop1)
print(student)

laptop2 = Student.Laptop("HP", "i7", 16)
student = Student("Vladimir", laptop2)
print(student)