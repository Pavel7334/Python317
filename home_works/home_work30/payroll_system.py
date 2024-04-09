from typing import List

from home_works.home_work30.employee import Employee


class PayrollSystem:
    """Система расчета заработной платы"""

    def calculate(self, employees: List[Employee]) -> None:
        print("Расчет заработной платы")
        print("=" * 50)
        for employee in employees:
            print(f"Заработная плата: {employee.id} - {employee.name}")
            print(f"- Проверить сумму: {employee.calculate_payroll()}")
            print()
