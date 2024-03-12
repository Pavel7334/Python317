class Car:
    def __init__(self):
        self.model = ""
        self.year = 0
        self.manufacturer = ""
        self.engine_power = 0
        self.color = ""
        self.price = 0.0

    def input_data(self):
        self.model = input("Введите модель машины: ")
        self.year = int(input("Введите год выпуска: "))
        self.manufacturer = input("Введите производителя: ")
        self.engine_power = float(input("Введите мощность двигателя: "))
        self.color = input("Введите цвет машины: ")
        self.price = float(input("Введите цену: "))

    def display_data(self):
        print(" Данные автомобиля ".center(40, "*"))
        print(f"Название модели: {self.model}")
        print(f"Год выпуска: {self.year}")
        print(f"Производитель: {self.manufacturer}")
        print(f"Мощность двигателя: {self.engine_power} л.с")
        print(f"Цвет машины: {self.color}")
        print(f"Цена: {self.price}")
        print("=" * 40)

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_manufacturer(self):
        return self.manufacturer

    def get_engine_power(self):
        return self.engine_power

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price

    def set_model(self, new_model):
        self.model = new_model

    def set_year(self, new_year):
        self.year = new_year

    def set_manufacturer(self, new_manufacturer):
        self.manufacturer = new_manufacturer

    def set_engine_power(self, new_engine_power):
        self.engine_power = new_engine_power

    def set_color(self, new_color):
        self.color = new_color

    def set_price(self, new_price):
        self.price = new_price


# Пример использования класса
car1 = Car()
car1.input_data()
car1.display_data()

# Пример доступа к отдельным полям через методы
print(f"\nМодель: {car1.get_model()}")
print(f"Год выпуска: {car1.get_year()}")
print(f"Производитель: {car1.get_manufacturer()}")
print(f"Мощность двигателя: {car1.get_engine_power()}")
print(f"Цвет машины: {car1.get_color()}")
print(f"Цена: {car1.get_price()}")

# Пример изменения значений полей через методы
car1.set_price(25000.0)
print("\nИзмененная цена машины:")
car1.display_data()


# Введите модель машины: X7 M50i
# Введите год выпуска: 2021
# Введите производителя: BMW
# Введите мощность двигателя: 530
# Введите цвет машины: white
# Введите цену: 10790000