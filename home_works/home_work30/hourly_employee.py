from employee import Employee


class HourlyEmployee(Employee):
    """Сотрудники с почасовой оплатой"""

    def __init__(self, kod: int, name: str, hours_worked: float, house_rate: float):
        super().__init__(kod, name)
        self.hours_worked: float = hours_worked
        self.house_rate: float = house_rate

    def calculate_payroll(self) -> float:
        return self.hours_worked * self.house_rate
