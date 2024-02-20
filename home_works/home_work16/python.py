def average_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, (int, float)):
            return {"numbers": args, "sum": sum(args), "average": sum(args) / len(args)}
        else:
            raise ValueError("Функция должна возвращать числовое значение")

    return wrapper


@average_decorator
def sum_and_average(*args):
    return sum(args)


# Вызываем функцию для получения суммы и среднего арифметического
result = sum_and_average(2, 3, 3, 4)
numbers = ', '.join(map(str, result['numbers']))

# Выводим сумму и среднее арифметическое
print(f"Сумма чисел: {numbers} = {result['sum']}")
print(f"Среднее арифметическое чисел: {numbers} = {result['average']}")
