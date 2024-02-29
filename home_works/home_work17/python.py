def format_name(full_name):
    parts = full_name.split()
    return f"{parts[0]} {parts[1][0]}.{parts[2][0]}."


print(format_name(input("Введите ФИО: ")))
