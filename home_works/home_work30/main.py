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


if __name__ == '__main__':
    from salary_employee import SalaryEmployee
    from hourly_employee import HourlyEmployee
    from comission_employee import CommissionEmployee

    salary_employee = SalaryEmployee(1, "Валерий Задорожный", 1500)
    hourly_employee = HourlyEmployee(2, "Илья Кромин", 40, 15)
    commission_employee = CommissionEmployee(3, "Николай Хорольский", 1000, 250)

    payroll_system = PayrollSystem()
    payroll_system.calculate([
        salary_employee,
        hourly_employee,
        commission_employee
    ])
