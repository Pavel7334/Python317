from employee import Employee


class SalaryEmployee(Employee):
    """Административные работники, имеют фиксированную зарплату"""

    def __init__(self, kod: int, name: str, weekly_salary: float):
        super().__init__(kod, name)
        self.weekly_salary: float = weekly_salary

    def calculate_payroll(self) -> float:
        return self.weekly_salary
