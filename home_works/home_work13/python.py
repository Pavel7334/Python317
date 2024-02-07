def getting_students(num):
    students = {}
    summa = 0
    for i in range(num):
        name = input(str(i + 1) + "-й студент: ")
        score = int(input("Балл: "))
        students[name] = score
        summa += score
    average = summa / num
    print(f"\nСредний балл: {average:.0f}. Студенты с баллом выше среднего:")
    for i in students:
        if students[i] > average:
            print(i)


getting_students(int(input("Количество студентов: ")))
