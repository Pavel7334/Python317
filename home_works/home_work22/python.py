class Car:

    def __init__(self, model: str, year: int, manufacturer: str, engine_power: int, color: str, price: float):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_power = engine_power
        self.color = color
        self.price = round(price, 2)

    def display_data(self):
        print()
        print(" Данные автомобиля ".center(40, "*"))
        print(f"Название модели: {self.model}")
        print(f"Год выпуска: {self.year}")
        print(f"Производитель: {self.manufacturer}")
        print(f"Мощность двигателя: {self.engine_power} л.с")
        print(f"Цвет машины: {self.color}")
        print(f"Цена: {self.price:.2f}")
        print("=" * 40)

    def get_model(self) -> str:
        return self.model

    def get_year(self) -> int:
        return self.year

    def get_manufacturer(self) -> str:
        return self.manufacturer

    def get_engine_power(self) -> int:
        return self.engine_power

    def get_color(self) -> str:
        return self.color

    def get_price(self) -> str:
        return "{:.2f}".format(self.price)

    def set_model(self, new_model: str):
        self.model = new_model

    def set_year(self, new_year: int):
        self.year = new_year

    def set_manufacturer(self, new_manufacturer: str):
        self.manufacturer = new_manufacturer

    def set_engine_power(self, new_engine_power: int):
        self.engine_power = new_engine_power

    def set_color(self, new_color: str):
        self.color = new_color

    def set_price(self, new_price: float):
        self.price = round(new_price, 2)


# Пример использования класса
car1 = Car(
    input("Введите модель машины: "),
    int(input("Введите год выпуска: ")),
    input("Введите производителя: "),
    int(input("Введите мощность двигателя: ")),
    input("Введите цвет машины: "),
    float(input("Введите цену: "))
)
car1.display_data()

# Пример доступа к отдельным полям через методы
print(f"\nМодель: {car1.get_model()}")
print(f"Год выпуска: {car1.get_year()}")
print(f"Производитель: {car1.get_manufacturer()}")
print(f"Мощность двигателя: {car1.get_engine_power()}")
print(f"Цвет машины: {car1.get_color()}")
print(f"Цена: {car1.get_price()}")

# Пример изменения значений полей через методы
car1.set_price(500000.00)
car1.set_color("black")
print("\nИзмененная цена и цвет машины:")
car1.display_data()
