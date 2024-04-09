from car.carclass import CarClass


class ElectroCar(CarClass):
    def __init__(self, brend, model, year, engine):
        super().__init__(brend, model, year, engine)
        self.battery = 100

    def description_battery(self):
        print(f"Электрокар {self.model} имеет батарею с {self.battery} % заряда")
