from salary_employee import SalaryEmployee


class CommissionEmployee(SalaryEmployee):
    """Торговые представители, фиксированная зарплата + комиссия"""

    def __init__(self, kod: int, name: str, weekly_salary: float, commission: float):
        super().__init__(kod, name, weekly_salary)
        self.commission: float = commission

    def calculate_payroll(self) -> float:
        fixed: float = super().calculate_payroll()
        return fixed + self.commission
