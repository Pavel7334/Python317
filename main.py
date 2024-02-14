from datetime import datetime

# first_name = "admin"
# First_name = "admin"
# print("Hello", first_name)
# age = 20
# print(age)
# print(type(first_name))
# print(type(age))
#
# a = 4
# b = 5
# a = b
# print(a, id(a))


# a = 5
# print(a)
# b = "7"
# print(a + int(b))


# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + " " + s2 + "___"
# print(s3)
# print(s3 * 3)


# a = 5
# b = 7
# c = 3
# print(f'Сумма: {a + b + c}')
#
# print(f'Произведение: {a * b * c}')
#
# print(f'Среднее арифметическое: {(a + b + c)/3}')

# numbers = (6 + 4) * (5 ** 2 + 7)
# print(numbers)


# num = 4321        # РАЗВЕРНУТЬ ЧИСЛО
# a = num % 10
# num = num // 10
# b = num % 10
# num = num // 10
# c = num % 10
# num = num // 10
# d = num % 10
# num = a * 1000 + b * 100 + c * 10 + d
# print(num)


# num = 4321
# res = num % 10 * 1000   # 1000
# num //= 10  # 432
# res += num % 10 * 100   # 200
# num //= 10
# res += num % 10 * 10    # 30
# num //= 10
# res += num % 10    # 4
# print(res)

# print(int(3.8))
# print(round(3.846, 2))


# a = '5.2'
# b = 10
# c = int(a) + b
# print(c)


# name = "Виктор"
# age = 28
# print("Меня зовут", name, ". Мне", age, "лет.")
# print("Меня зовут" + name + ". Мне" + str(age) + "лет.")
# print("Меня зовут", name, ". Мне", age, "лет.", sep="---", end=" ")
# print("Hello")


# name = input("Введите имя: ")
# city = input("Введите город: ")
# print(name, city)


# num = input("Введите число: ")
# power = input("Введите степень: ")
# res = int(num) ** int(power)
# print("Число", num, "в степени", power, "равна:", res)


# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# c = int(input("Введите третье число: "))
# d = int(input("Введите четвертое число: "))
# print("1:", a)
# print("2:", b)
# print("3:", c)
# print("4:", d)
# result = round(((a + b)/(c + d)), 2)
# print(result)


# False => "", 0, 0.0, False

# print(bool("python"))
# print(bool(""))
# print(bool(10))
# print(bool(0.0))
# print(bool(False))
# print(bool(None))


# test = None
# print(test)
# test = 5
# print(test)
# test = "hello"
# print(test)
# test = [2,3,5,6,7,8]
# print(test)


# print(7 == 7)
# print(7 == "7")
# print(2 + 5 == 7)
# print(2 + 5 != 7)
# print(8 > 5)
# print(8 < 5)
# print(8 >= 8)
# print(8 <= 8)
# print("привет" > "ПРИВЕТ")


# print(5 - 3 == 2 and 1 + 3 == 4)
# print(5 - 3 == 2 and 1 + 3 == 4)
# print(not 9 - 5)
# print(not 9 - 9)


# cnt = 5
# if cnt < 10:
#     cnt += 1
#     print(cnt)


# age = int(input("введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")


# num1 = int(input("Введите первую сторону: "))
# num2 = int(input("Введите вторую сторону: "))
# num3 = int(input("Введите третью сторону: "))
#
# if num1 == num2 == num3:
#     print('Треугольник равносторонний')
# elif num1 == num2 != num3:
#     print('Треугольник равнобедренный')
# else:
#     print('Треугольник разносторонний')


# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
#
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресение")
# else:
#     print("Такого дня недели не существует!")


# crow = int(input("Введите количество ворон: "))
# if 0 <= crow <= 9:
#     print("На ветке", end=" ")
#     if crow == 1:
#         print(crow, 'ворона')
#     elif 2 <= crow <= 4:
#         print(crow, 'вороны')
#     else:
#         print(crow, 'ворон')
# else:
#     print("Ошибка ввода данных")


# def func(num):
#     if num % 10 == 1 and num % 100 != 11:
#         return f'{num} копейка'
#     elif num % 10 in [2, 3, 4] and num % 100 not in [12, 13, 14]:
#         return f'{num} копейки'
#     else:
#         return f'{num} копеек'
#
#
# print(func(int(input())))


# n = int(input())
# print(n, 'копе' + ['ек', 'йка', 'йки', 'йки', 'йки', 'ек', 'ек', 'ек', 'ек', 'ек'][(n // 10 % 10 != 1) * n % 10])
#
#
# num = int(input())
# if 1 <= num <= 99:
#     if num % 10 == 1 and num % 100 != 11:
#         print(num, 'копейка')
#     elif num % 10 in [2, 3, 4] and num % 100 not in [12, 13, 14]:
#         print(num, 'копейки')
#     else:
#         print(num, 'копеек')
# else:
#     print("Ошибка ввода данных")


# password = "admin"
#
# match password:
#     case 'admin':
#         print("Администратор")
#     case 'user':
#         print("Пользователь")
#     case _:
#         print("Пароль не верен")


# day = 'воскресение'
#
# time = 11
#
# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 16:
#         print("Рабочий день")
#     case 'суббота' | 'воскресение' if 9 <= time <= 12:
#         print("Рабочий день")
#     case 'суббота' | 'воскресение':
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует или не рабочее время")


# a, b = 10, 20
#
# minim = a if a < b else b
# print(minim)


# a, b = 10, 20
# print("a == b" if a == b else "a > b" if a > b else "b > a")


# a, b = int(input("Введите первое число")), int(input("Ввведите второе число"))
# print("На ноль делить нельзя!!!" if b == 0 else a / b)


# try:
#     a = int(input("Введите целое число: "))
#     print(a * 2)
# except ValueError:
#     print("Что то пошло не так")


# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")


# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки и нельзя делить на ноль")
# else:   # когда в блоке try не возникло исключений
#     print("Всё нормально. Вы ввели числа ", n, "и", m)
# finally:    # выполняется в любом случае
#     print("Конец программы")


# n = input("Введите делимое: ")
# m = input("Введите делитель: ")
#
# try:
#     print(int(n) + int(m))
# except ValueError:
#     print(n + m)


# n = input("Введите делимое: ")
# m = input("Введите делитель: ")
#
# try:
#     n = int(n)  # '9 => 9
#     m = int(m)
# except ValueError:
#     n = str(n)
# finally:
#     print(n + m)


# i = 0
#
# while i < 5:
#     print("i =", i)
#     i += 1


# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print("i =", i)
#     i += 1


# n = int(input("Укажите кол-во символов: "))
# print("*" * n)


# n = int(input("Укажите кол-во символов: "))
# i = 0
#
# while i < n:
#     print("*", end="")
#     i += 1


# n = int(input("Укажите кол-во символов: "))
# i = 0
#
# while i < n:
#     if i % 2 == 0:
#         print("+", end="")
#     else:
#         print("-", end="")
#     i += 1


# n = int(input("Укажите кол-во символов: "))
# while n > 0:
#     print("*", end="")
#     n -= 1


# 1 - 5 => 1 + 3 + 5

# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапазона: "))
#
# res = 0
#
# while a <= b:
#     if a % 2:
#         res += a
#     a += 1
# print("Сумма целых нечётных чисел: ", res)


# n = input("Введите целое число: ")
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число")
#
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")


# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")


# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1


# while True:
#     n = int(input("Введите положительное число: "))
#     if n < 0:
#         break


# res = 1
# while True:
#     n = int(input("Введите число: "))
#     if n == 0:
#         break
#     res *= n
# print("Результат:", res)


# i = 0
#
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)


# i = 1
#
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i += 1


# i = 1                 # ТАБЛИЦА УМНОЖЕНИЯ
#
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1


# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if j % 2 == 0:      # if i % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1

# +-+-+-+-+-+-+-+-
# +-+-+-+-+-+-+-+-
# +-+-+-+-+-+-+-+-
# +-+-+-+-+-+-+-+-
# +-+-+-+-+-+-+-+-


# j = 1
# while j < 6:
#     print(" " * j, "*")
#     j += 1

# *
#  *
#   *
#    *
#     *


# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(" ", end="")
#         j += 1
#     print("*")
#     i += 1


# j = 0
# while j < 5:
#     print("-" * j, "*", sep="")
#     j += 1


# for color in "red", "yellow", "green", 1, 20, 0.3:
#     print(color)


# print(range(2, 5, 2))

# range(start, stop, step)


# for i in range(9):
#     print(i, end=" ")
#
# print()
#
# i = 0
# while i < 9:
#     print(i, end=" ")
#     i += 1


# a = int(input("Введите целое число: "))
#
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")


# for i in range(10, 100):
#     if i // 10 == i % 10:
#         print(i, end=" ")


# for i in range(3):
#     print(i)
# else:
#     print("done")


# w = 16       #  int(input("Введите длину прямоугольника: "))
# h = 4        #  int(input("Введите высоту прямоугольника: "))
# for i in range(h):  # 4
#     for j in range(w):  #
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()


# numbers = [4.3, 8.2, 2.8, 6.6, 1.5, 9.3, 5.7]
#
#
# min_num = numbers[0]
# for num in numbers:
#     if num < min_num:
#         min_num = num
#
#
# max_num = numbers[0]
# for num in numbers:
#     if num > max_num:
#         max_num = num
#
# summa_num = 0
# for num in numbers:
#     summa_num += num
#
#
# print("Среднее арифметическое: ", round(summa_num/len(numbers), 2))
# print("Минимальное число: ", min_num)
# print("Максимальное число: ", max_num)


# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# s = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         s += a[i]
# print(s)


# lst = list(range(10, 1000000, 10))
# print(lst)
# for i in range(len(lst)):
#     print(lst[i], end=" ")
# print()
# for i in lst:
#     print(i, end=" ")


# lst = list(range(10, 10000000, 10))
#
# def timeit(func):
#     def wrapper():
#         start = datetime.now()
#         result = func()
#         print(datetime.now() - start)
#         return result
#     return wrapper
#
#
# @timeit
# def one():
#     l = []
#     for i in range(len(lst)):
#         l.append(i)
#     return l
#
#
# @timeit
# def two():
#     li = []
#     for i in lst:
#         li.append(i)
#     return li
#
# l1 = one()
# l2 = two()


# n = list(range(21, 41))
# print(n)
# count = s = 0
# for i in n:
#     if i % 2 == 0:
#         count += 1
#     else:
#         s += i
# print("Кол-во четных элментов списка:", count)
# print("Сумма нечетных элементов списка:", s)


# n = list(range(21, 41))
# print(n)
# i = 2
# print(n[i])
# print(n[i - 1])


# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)

# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")

# for i in a:
#     if i > i + 1:
#         print(i, end=" ")


# a = [7, 9, 3, 1, 2]
# print(id(a[0]))
# print(id(a[1]))
# a[0], a[1] = a[1], a[0]
# print(id(a[0]))
# print(id(a[1]))


#                                               СРЕЗЫ - список[start:stop:step]

# s = "Hello World!"
# print(s[6:-1])


# s = list(range(1, 8))
# print(s)
# print(s[::2])
# print(s[1::2])
# print(s[1::2])
# print(s[:1])
# print(s[-1:])
# print(s[-3:])
# print(s[4:1:-1])
# print(s[2:5])

# s = [1, 2, 3, 4, 5, 6, 7]
# print(s)
# s[1:3] = [0, 0, 0, 0]
# print(s)
# s[1:2] = [20]
# print(s)
# s[2:5] = []
# print(s)
# del s[1]
# print(s)


# Методы списков
# dir(list)
# s = [9, 7, 8, 4, 6, 5, ]
# print(s)
# # s[len(s):] = [12]     ДОБАВИТЬ В КОНЕЦ СПИСКА ЧЕРЕЗЕ СРЕЗ
# s.append(12)            # добавляет один элемент в конец списка
# print(s)
# s.extend([1, 2, 3])     # добавляет любое количество элементов в конец списка
# print(s)
# s.extend("add")
# print(s)
# s.insert(3, 'Hello')    # добавляет элемент в список в заданный индекс (первый параметр), значение (второй параметр)
# print(s)


# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
#
# s = []
# n = int(input("Кол-во элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     s.insert(0, x)
# print(s)


# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []

# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(j)
#             break
#
# print(c)

# for element in a:
#     if element not in c and element in b:
#         c.append(element)
#
# print(c)

# a = [1, 2, 3]
# b = [11, 22, 33, 4, 5]
# c = []
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])
# print(c)


# a = [1, 2, 3]
# b = [11, 22, 33, 4, 5]
# c = []
# if len(a) > len(b):
#     a, b = b, a
#
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])
# print(c)


# a = [1, 3, 2, 3, 4, 3, 5]
# print(a)
# a.remove(3)     #   удаляет  из списка по значению
# print(a)


# a = [1, 3, 2, 3, 4, 3, 5]
# print(a)
# last = a.pop()  # удаляет послдний элемент из списка и возвращает удалённый элемент
# print(last)
# print()


# s = []
# for num in range(int(input("Введите элементы списка: "))):
#     x = int(input("-> "))
#     s.append(x)
# k = int(input("Введите индекс: "))
# s.pop(k)
# print(s)


# a = [1, 5, 3, 2, 3, 4, 3, 5]
# print()
# num = a.count(5)    # возвращает количество заданных значений в списке
# print(num)
#
# ind = a.index(2, 3)    # показывает где располагается(индекс) элемент
# print(ind)

# a = [1, 5, 3, 2, 3, 4, 3, 5]
# s = ["Виталий", "Сергей", "Александр", "Анна"]
# s.sort(reverse=True, key=len)
# print(s)


#                               Генерация случайных данных

import random

# print(random.random())  # от 0 до 1 (не включительно)
# print(random.randint(0, 9))  # от 0 до 9 (включительно)
# print(random.randrange(9))  # от 0 до 9 (не включительно)   randrange(start, stop, step)
# print(round(random.uniform(10.5, 25.5), 2))
# print(random.uniform(10.5, 25.5))
#
# city_list = ["Москва", "Новосибирск", "Воронеж", "Сочи", "Екатеринбург"]
# print(random.choice(city_list)) # выбирает один город
# print(random.choices(city_list, k=3))  # выбирает несколько
#
#
# s = [20, 30, 40, 50, 60, 70, 80, 90]
# print(random.choice(s))
# random.shuffle(s)   # смешивает элементы
# print(s)


# mas = [random.randint(0, 100) for i in range(10)]
# # mas = ['a', 'b', 'c']
# print(mas)
# print(len(mas))
# print(min(mas))
# print(max(mas))
# # print(sum(mas))


# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# summa = max(mas)
# print(summa)
# mas.remove(summa)
# mas.insert(0, summa)
# print(mas)

# array = [random.randint(-20, 20) for i in range(20)]
# array.sort(reverse=True)
# print(array)

# array = [random.randint(0, 100) for i in range(10)]
# print(array)
# minimum = min(array)
# print("Min: ", minimum)
# ind = array.index(minimum)
# print(ind)
# # del array[:ind]
# print(array[ind:])


# lst = [2]
# if lst:
#     print("Список не пустой")

#
# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [random.randint(0, 10) for i in range(n1)]
# b = [random.randint(0, 10) for i in range(n2)]
# print("Первый список:", a)
# print("Первый список:", b)
# c = a + b
# print(c)


# c = []

# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
# print(c)

# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
# print(c)

# c = [min(a), min(b), max(a), max(b)]
# print(c)

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print(m)
# print(len(m))
# print(m[1][2])
# print()

# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()
# print()
#
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()


# w, h = 5, 3
# # matrix = [[0 for x in range(w)]for y in range(h)]
# # print(matrix)
#
# matrix = []
# for y in range(h):
#     new_row = []
#     for x in range(w):
#         new_row.append(0)
#     matrix.append(new_row)
# print(matrix)
#
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()

# for x, y in [1, 2], [3, 4], [5, 6], [7, 8]:
#     print(x, "+", y, "=", x + y)


# w, h = 5, 3
# matrix = [[random.randint(1, 100)for y in range(w)] for y in range(h)]
# print(matrix)
#
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()

# w, h = 3, 4
# count = 0
# matrix = [[random.randint(-20, 10) for y in range(w)] for y in range(h)]
#
# for row in matrix:
#     for x in row:
#         print(x, end="\t\t")
#         if x < 0:
#             count += 1
#     print()
# print("Количество отрицательных элементов:", count)

# import math as m
#
# # print(math.sqrt(4))
# # print(math.pi)
# print(m.ceil(3.2))
# print(m.floor(3.8))

# from math import pi
#
# radius = (int(input("Введите радиус окружности: ")))
# print("Длина окружности:", round(2 * pi * radius, 2))

# from math import sqrt
#
# a = int(input("Введите первый катет: "))
# b = int(input("Введите второй катет: "))
# print(sqrt(a ** 2 + b ** 2))

import time

# import locale
#
# locale.setlocale(locale.LC_ALL, "bel")
#
# seconds = time.time()
# print(seconds)
# print(time.ctime())
# print(time.ctime(1705512684))
# res = time.localtime()
# print(res)
# print(res.tm_mday, ".0", res.tm_mon, ".", res.tm_year, sep="")
#
# print(time.strftime("Сегодня: %B %d, %Y"))
# print(time.strftime("%B %d, %Y", time.localtime(345312543)))
# print(time.strftime("%d/%m/%Y, %H:%M:%S"))

# pause = 5
# print("Программа запущена")
# time.sleep(pause)
# print(pause, "секунд")

# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res)


# def hello(name):
#     print("Hello", name)
#
#
# hello("Irina")
#
#
# def get_sum(a, b):
#     print(a + b)
#
#
# a = 2
# b = 5
# get_sum(a, b)
# n = 6
# get_sum(a, n)

# def foo(a, b):
#     if a > b:
#         return a - b
#     else:
#         return a + b
#
#
# c = foo(int(input()), int(input()))
# print(c)

# def cube(a):
#     return a * a * a
#
#
# for i in range(1, 11):
#     print(i, "в кубе =", cube(i))

# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#
#     start = lst.pop()
#     end = lst.pop(0)
#     lst.append(end)
#     lst.insert(0, start)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))


# lst_1 = [1, 2, 3]
# lst_2 = [9, 12, 33, 54, 105]
# lst_3 = ["c", "л", "о", "н"]
#
#
# def change(lst):
#     res = []
#     for i in range(len(lst)):
#         if i == 0:
#             res.append(lst[-1])
#         elif i == len(lst) - 1:
#             res.append(lst[0])
#         else:
#             res.append(lst[i])
#     return res
#
#
# print("Результат:")
# print(change(lst_1))
# print(change(lst_2))
# print(change(lst_3))


# def func(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# print(func(10, 5))
# print(func(5, 10))
# a = 5
# b = 10
# if func(a, b):
#     print("Первое число больше второго")
# else:
#     print("Второе число больше второго")


#                                                УСТАНОВКА ПАРОЛЯ
# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         if "a" <= ch <= "z":
#             has_lower = True
#         if "0" <= ch <= "9":
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Это надёжный пароль")
# else:
#     print("Это ненадёжный пароль")

# if "!"<= ch <= "/" or ":"<= ch <= "@" or "["<= ch <="`" or "{"<= ch <= "~":
#     has_sym = True


# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, d=2))


# def set_param(c=20, s='-'):
#     print(s * c)
#
#
# set_param()
# set_param(7)
# a = "#"
# set_param(s=a)

# def digit_sum(n, even=True):
#     s = 0
#     while n > 0:
#         # cur_digit = n % 10  # выводит последнюю цифру
#         # print(cur_digit)
#         cur_digit = n % 10
#         if even and cur_digit % 2 == 0:
#             s += cur_digit
#         if not even and cur_digit % 2 != 0:
#             s += cur_digit
#         n //= 10
#     return s
#
#
# print("Сумма чётных цифр: ")
# print(digit_sum(9874023))
# print(digit_sum(38271))
# print(digit_sum(123456789))
#
# print("Сумма нечётных чисел: ")
# print(digit_sum(9874023, even=False))
# print(digit_sum(38271, even=False))
# print(digit_sum(123456789, even=False))


# def display_info(name, age, nm):
#     print("Name:", name, "\nAge:", age)
#
#
# # display_info("Ira", 23)
# # display_info(23, "Ira")
# # display_info(age=23, name="Ira")
# display_info(nm="Igor", age=23, name="Ira")


# a = "Hello"
# b = "Hello"
# print(a, id(a))
# print(b, id(b))
# print(a == b)  # True
# print(a is b)  # True
#
# lst1 = [1, 2, 3]
# lst2 = [1, 2, 3]
# print(lst1, id(lst1))
# print(lst2, id(lst2))
# print(lst1 == lst2)  # True
# print(lst1 is lst2)  # False

#   Изменяемые объекты - list
#   Неизменяемые объекты - int, float, bool, str

# lst1 = [1,2,3]
# print(lst1, id(lst1))
# lst1.append(4)
# print(lst1, id(lst1))

#           Кортежи

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())
#
# a = "red", "blue", "green"
# print(a)
# print(type(a))

# a = (5,)
# print(a)
# print(type(a))

# a = tuple("Hello")
# a = tuple([1, 5, 8, 9, 6])
# print(a)
# print(type(a))
# print(a[0])
# print(a[1:3])

# from random import randint


# s = tuple(randint(20, 40) for i in range(5))
# print(s)

# res = tuple(2 ** i for i in range(1, 13))
# print(res)

# t1 = tuple("hello")
# t2 = tuple("world")
# t3 = t1 + t2
# print(t3)
# print(t3.count('l'))
# print(t3.count('a'))
# # print(t3.index('l', 4))
#
# ch = "a"
# try:
#     print(t3.index(ch))
# except ValueError:
#     print("Такого символа в кортеже не существует")
# for i in t3:
#     print(i, end=" ")


# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1)
#             return tpl[first:second + 1]
#         else:
#             return tpl[tpl.index(el):]
#     return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))
# from random import randint
#
#
# def foo():
#     t1 = tuple(randint(0, 5) for i in range(10))
#     t2 = tuple(randint(-5, 0) for i in range(10))
#     c = res.count(0)
#     return res, c
#
#
# t1 = tuple(randint(0, 5) for i in range(10))
# t2 = tuple(randint(-5, 0) for i in range(10))
# print(foo(t1, t2))


from random import randint

# def run(a, b):
#     return tuple(randint(a, b) for i in range(10))
#
#
# tpl1 = run(0, 5)
# tpl2 = run(-5, 0)
# print(tpl1)
# print(tpl2)

# from random import randint
#
#
# def tpl(minus=False):
#     if minus:
#         t = tuple(randint(-5, 0) for i in range(10))
#     else:
#         t = tuple(randint(0, 5) for i in range(10))
#     return t
#
#
# t1 = tpl()
# t2 = tpl(True)
# t3 = t1 + t2
# print(t1)
# print(t2)
# print(t3)
# print("0 =", t3.count(0))


# t = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world'])
# print(t, id(t))
# t[4][0] = "new"
# t[4].append('hi')
# print(t, id(t))


# t = (1, 2, 3)
# x, y, z = t     # распаковка кортежа
# print(x, y, z)

# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# # user = get_user()
# # print(user)
# # print(user[0])
# # print(user[1])
# # print(user[2])
#
# name, age, married = get_user()
# print(name, age, married)

# def func(lst):
#     return f"Сумма = {sum(lst)}\nКоличество = {len(lst)}"
#
#
# print(func([2, 9, 6, 5, 8, 7, 5, 8, 7, 1, 4, 5, 4]))
#
#
# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
# print(countries)
#
# for country in countries:
#     country_name, country_population, cities = country
#     print("\nСтрана: ", country_name, ", население = ", country_population, sep="")
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород: ", city_name, ", население = ", city_population, sep="")


#   МНОЖЕСТВО (set)

# s = {'banana', 'apple', 'orange', 'banana', 'apple', 'orange'}
# print(s)
# print(type(s))

# s = {i * i for i in range(15)}
# print(s)

# a = set("Hello")
# print(a)
# a.add("a")
# print(a)
# el = "e1"
# if el in a:
#     a.remove(el)
# print(a)
# a.discard("o")
# print(a)
# a.pop()
# print(a)


# tpl = tuple(input("Введите по порядку, без пробелов, элементы кортежа: "))
# print(tpl)
# res = []
# for el in tpl:
#     if el not in res:
#         res.append(el)
# for i in res:
#     print("Количество", i, "=", tpl.count(i))

# print("Данные для добавления на GitHub")
#
# print("Данные внесенные с другой машины")


#                                               GIT

# git --version
# git --help
#
# git init
# - создание нового репозитория (один раз для одного репозитория)
#
# git status
# - просмотр состояния репозитория
#
# git add -A
# 	-A, --all - все файлы, которые находятся в папке и всех подпапках
# 	main.py - один файл
# 	. - все файлы из текущей директории
# - отслеживание изменения файлов
#
# git config --global user.name "new user"
# 		   --local
#
# git config --global user.email "test@mail.ru"
#
# git commit -m "first commit"
# - создание контрольной точки состояния репозитория
#
# .gitignore
#
# git add .
# git commit -m "added gitignore"
#
# Ветки
#
# git branch
# - просмотр веток
#
# git branch test
# - создаем ветку
#
# git branch -D test
# - удаление ветки
#
# git branch readme
#
# git checkout readme
# - перейти на ветку
#
# readme.md
#
#
# master       readme
# main.py  ->   main.py
# 		<-	  readme.md
#
# git merge readme
# - слияние веток
#
# git log
# - история коммитов
#
# токен
#
# win + R => control
# (Панель управления)
#
# Диспечер учетных данных
# Учетные данные Windows
# Общие учетные данные -> Добавить
# https://github.com
#
#
# git remote add origin https://github.com/Helen-prog/Python317.git
# git push -u origin master
#
# 75d6a172128ea34beeeb00a21b1a82b736b3ab58
#
# 0) git status
# 1) git add .
# 2) git commit -m "added print"
# 3) git push
# - с локального репозитория переносит файлы на удаленный репозиторий
# 
# git clone https://github.com/Helen-prog/Python317.git
# - клонирование репозитория
#
# git pull
# - забирает изменения с удаленного репозитория в локальный

# s = ['ab_1', 'ac_2', 'bc_1', 'bc_2']

# a = [x for x in s if 'a' not in x]
# a = ['A' + x[1:] if x[0] == 'a' else 'B' + x[1:] for x in s]
# a = ['A' + x[1:] if x[0] == 'a' else 'B' + x[1:] for x in s if x[1] == 'c']
# print(a)

# print(['A' + x[1:] if x[0] == 'a' else 'B' + x[1:] for x in ['ab_1', 'ac_2', 'bc_1', 'bc_2'] if x[1] == 'c'])

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# # c = a | b     # сложение уникальных значений
# # c = a & b       # пересечение
# # c = a - b         # вычитание элементов из a
# c = a ^ b           # разные значения в обоих переменных
# # c = a.union(b)
# print(c)
#
# a -= b
# print(a)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# # s = s1.union(s2, s3, s4, s5, s6, s7)
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(s)
# print(len(s))
# print(min(s))
# print(max(s))

# s1 = "Hello"
# s2 = "How are you"
#
# s = set(s1) & set(s2)
# print(s)
# for i in s:
#     print(i, end=" ")


# s1 = "Python"
# s2 = "Programming language"
#
# print(s1 - s2)
#
# # for i in s:
# #     print(i, end=" ")

# c1 = set("Python")
# c2 = set("Programming language")
# print(c1-c2)

# drawing = {'Марина', 'Женя', 'Света'}
# music = {'Костя', 'Женя', 'Илья'}
#
# one_hobby = drawing ^ music
# print(one_hobby)
# both_hobby = drawing & music
# print(both_hobby)
#
# drawing = drawing - both_hobby
# print(drawing)


# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# print(a >= b)

# s = frozenset([1, 2, 3, 4, 5, 6])
# print(s)

#                                                      СЛОВАРИ!!!!

# s = [1, 2, 3]
# d = {"one": 1, "two": 2, "thee": 3}
# print(s[1])
# print(d["two"])
#
# s1 = ["one", "two", "three"]
# d1 = {1: "one", 2: "two", 3: "three"}
# print(s1[1])
# print(d1[2])

# d = {(1, 2, 3, (2, 3)): "Кортеж"}
#
# print(d)

# d = {'one': 1, 'two': 2}
# print(d)
# print(type(d))
#
# c = dict(one=1, two=2)
# print(c)
# print(type(c))

# d1 = dict([("one", 1), ("two", 2)])
#
# print(d1)

# d = {x: x ** 2 for x in range(7)}
# print(d)

# d = {"one": 1, "two": 2, "thee": 3}
# print(d)
# # print("two" in d)
# # print(len(d))
# #
# # for key in d:
# #     print(key, "->", d[key])
# key = "one"
# del d[key]
# # try:
# #     print(d[key])
# # except KeyError:
# #     print("Такого ключа не существует")
# print(d)

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# res = 1
# for x in d:
#     res *= d[x]
# print(res)

# d = {x: input("-> ") for x in range(1, 5)}
#
# print(d)
# try:
#     dislike = int(input("Какой элемент исключить: "))
#     del d[dislike]
# except (KeyError, ValueError):
#     print("Такого ключа не существует")
# print(d)

# def is_palindrome(string: str) -> bool:
#     if string != string[::-1]:
#         return False
#     return True
#
#
# print(is_palindrome("aboba"))
# print(is_palindrome("axc"))


# goods = {
#     "1": ["Core-i3-4330", 9, 4500],
#     "2": ["Core i5-4670K", 3, 8500],
#     "3": ["AMD FX-6300", 6, 3700],
#     "4": ["Pentium G3220", 8, 2100],
#     "5": ["Core i5-3450", 5, 6400],
# }
#
# for key in goods:
#     print(key, ") ", goods[key][0], " - ", goods[key][1], " шт. по ", goods[key][2], " руб.", sep="")
#
# while True:
#     n = input("№: ")
#     if n != "0":
#         if n in goods:
#             while True:
#                 try:
#                     count = int(input("Кол-во: "))
#                     goods[n][1] += count
#                     break
#                 except ValueError:
#                     print("Значение некорректное. Введите число")
#         else:
#             print("Такого ключа не существует")
#     else:
#         break
#
#
# for key in goods:
#     print(key, ") ", goods[key][0], " - ", goods[key][1], " шт. по ", goods[key][2], " руб.", sep="")


# d = {'x1': 3, 'x2': 7, 'x3': 5}
# print(d)
# # del d['x1']
# # d['x4'] = 10
# # print(d)
# # a = {'one': 1}
# # c = d | a
# # print(c)
# print(d.values())
# print(d.keys())
# print(d.items())
# # for key, value in d.items():
# #     print(key, "->", value)
# print(list(d))
# print(list(d.values()))
# print(list(d.items()))

# d = {'x1': 3, 'x2': 7, 'x3': 5}
#
# d2 = d.copy()
# print("d =", d)
# print("d2 =", d2)
#
# d2["x4"] = 10
# print(d2)
# print(d)

# d = {'x1': 3, 'x2': 7, 'x3': 5}
# print(d["x1"])
# value = d.get("x4", "Такого ключа не существует")
# print(value)
# item = d.pop("x4", "Такого ключа не существует")
# print(item)
# item2 = d.popitem()
# print(item2)
# print(d)
#
# d.clear()
# print(d)

# d = {'x1': 3, 'x2': 7, 'x3': 5}
# print(d)
# # item = d.setdefault("x4", 10)
# # print(item)
# # print(d)
# a = {"one": 1, "two": 2}
# a = list(a.items())
# print(a)
# d.update(a)
# print(d)


# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# z = x | y
# print(z)

# d = dict.fromkeys(['a', 'b', 'c'], 100)
# print(d)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# d['location'] = d.pop('city')
# print(d)
# d2 = dict()
# d2['name'] = d.pop("name")
# d2['salary'] = d.pop("salary")
# print(d)
# print(d2)

# d = {
#     'first': {
#         1: "one",
#         2: "two",
#         3: "three"
#     },
#     'second': {
#         4: "four",
#         5: "five"
#     }
# }
#
# print(d)
#
# for x in d:
#     print(d[x])
#     for y in d[x]:
#         print("\t", y, ":", d[x][y])


# d = {
#     'first': {
#         1: {
#             11: "abc",
#             12: "abc",
#             113: "abc",
#         },
#         2: {
#             11: "abc"
#         },
#         3: {
#             11: "abc"
#         }
#     },
#     'second': {
#         4: {
#             11: "abc"
#         },
#         5:  {
#             11: "abc"
#         }
#     }
# }
# print(d)
#
# for x in d:
#     print(x)
#     for y in d[x]:
#         print("\t", y)
#         for z in d[x][y]:
#             print("\t\t", z, ":", d[x][y][z])

# d = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
# d2 = {key: value for key, value in d.items() if value <= 2}
# print(d2)

# a = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
#
# d = dict()
# s = None
#
# for i in a:
#     if type(i) == str:
#         d[i] = []
#         s = i
#     else:
#         d[s].append(i)
# print(d)


# num = [2, 5, 7, 2, 7, 88, 22, 3, 45, 767, 99, 22]
#
# N = 10
# a = []
# for i in num:
#     a.append(i)
# print(a)
#
# for i in range(N - 1):
#     for j in range(N - i - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
#
# print(a)


# def bubble_sort(list1):
#     for i in range(0, len(list1) - 1):
#         for j in range(len(list1) - 1):
#             if list1[j] > list1[j + 1]:
#                 temp = list1[j]
#                 list1[j] = list1[j + 1]
#                 list1[j + 1] = temp
#     return list1
#
#
# list1 = [5, 3, 8, 6, 7, 2, 44, 22, 77, 99, 2234, 897]
# print(list1)
# print(bubble_sort(list1))


#                                                      ZIP


# one = [1, 2, 3]
# two = ["one", "two", "three"]
#
# d = dict(zip(one,two))
# print(d)
#
# # lst = list(zip(one, two))
# # print(lst)
#
# lst = list(zip(one))
#
# print(lst)
#
# f = {k: v for k, v in zip(two, one)}
# print(f)


# one = {"name": "Igor", "surname": "Doe", "job": "Consultant"}
# two = {"name": "Irina", "surname": "Smith", "job": "Manager"}
# three = {"name": "Irina", "surname": "Smith", "job": "Manager"}
#
#
# for (k1, v1), (k2, v2), (k3, v3) in zip(one.items(), two.items(), three.items()):
#     print(k1, "->", v1)
#     print(k2, "->", v2)
#     print(k3, "->", v3)


# lst = [(1, 'one'), (2, 'two'), (3, 'three')]
# d = {1: 'one', 2: 'two', 3: 'three'}
# a, b = zip(*d)
# print(a)
# print(b)
# print(d)

# a = {1: 'one', 2: 'two'}
# b = {3: 'three', 4: 'four'}
# print({**a, **b})
#
#
# for k, v in {**a, **b}.items():
#     print(k, "->", v)


# data = [5, 7, 9, 4, 1, 3, 5, 8, 6, 4]
# data = ["red", "green", "blue"]
#
# for num, color in enumerate(data, 1):
#     print(num, ") ", color, sep="")

# j = 1
# for i in data:
#     print(j, ")", i, sep="")
#     j +=1

# a = [1, 2, 3]
#
# b = [*a, 4, 5, 6]
#
# print(b)


# def func(*args):
#     return args
#
#
# print(func(5, 6, 7, 8, 9, 0, "abc"))
# print(func())


# def summa(*args):
#     res = 0
#     for i in args:
#         res += i
#     return res
#
#
# print(summa(1, 4, 5, 4, 3, 6, 6, 54, 6, 6, 4, 6, 6, 6, 4))


# def di(*di):
#     dictionary = {}
#     for i in di:
#         dictionary.update({i: i})
#
#     return dictionary
#
#
# print(di(1, "one", 3, 4, "two", 6, 7, (8, 3, 5, 6, 78)))


# def foo(*args):
#     average = sum(args) / len(args)
#     print(average)
#     res = []
#     for num in args:
#         if num < average:
#             res.append(num)
#
#     return res
#
#
# print(foo(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(foo(3, 6, 1, 9, 5))


# def func(a, *args):
#     return a, args
#
#
# print(func(5))
# print(func(5, 9, 8, 7, 6))

# def print_scores(student, *scores):
#     print("Name: ", student)
#     for score in scores:
#         print(score, end=" ")
#     print()
#
#
# print_scores("Roman", 5, 4, 3, 5, 4, 5, 5, 3, 5)
# print_scores("Nikita", 5, 5, 3, 5)


# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(name="Python"))


# def intro(**kwargs):
#     for k, v in kwargs.items():
#         print(k, "is", v)
#     print()
#
#
# intro(name="Irina", surname="Sharma", age=22)
# intro(name="Igor", surname="Wood", email="igor@gmail.com", age=22, phone=987654321)


# def func(a, b, *args, dd=5, cc=7, **kwargs):
#     return a, b, args, kwargs, dd, cc
#
#
# print(func(1, 2, 3, 4, 5, aa=1, bb=2, cc=3))


# def db(**kwargs):
#     my_dict.update(**kwargs)
#
#
# my_dict = {"one": "first"}
# db(k1=22, k2=31, k3=11, k4=91)
# db(name="Bob", age=31, weight=61, eyes_color="grey")
# print(my_dict)

# name = "Tom"  # Глобальная переменная
# surname = ""
#
#
# def hi():
#     global name, surname
#     name = "Sam"  # Локальная переменная
#     surname = "Johnson"
#     print("Hello", name, surname)
#
#
# def bye():
#     print("Good bye", name)
#
#
# print(name)
# hi()
# bye()
# print(name)
# print(surname)

# i =5
#
#
# def foo(args=i):
#     print(args)
#
# i = 6
# foo() # 5


# def func(a):  # a = 3
#     x = 2
#
#     def inner():
#         x = 6
#         print("x:", x)
#         return a + x    # 3 + 6
#
#     return inner()
#
#
# print(func(3))


# def outer(who):
#     def inner():
#         print("Hello", who)
#
#     inner()
#
#
# outer("World!")


# def fun1():
#     a = 6
#
#     def fun2(b):
#         a = 4
#         print(a + b)
#
#     print("a: ", a)
#     fun2(4)
#
#
# fun1()


# x = 25
# t = 0
#
#
# def fn():
#     global t
#     a = 30
#
#     def inner():
#         nonlocal a
#         a = 35
#
#     inner()
#     t = a
#
#
# fn()
# q = x + t
#
# print(q)


# def fn1():
#     x = 25
#
#     def fn2():
#         x = 33
#
#         def fn3():
#             x = 55
#
#         fn3()
#         print("fn2.x =", x)
#
#     fn2()
#     print("fn1.x =", x)
#
#
# fn1()


# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#         # print("a:", a)
#         # print("b:", b)
#
#     inner()
#     return [a, b]
#
#
# print(outer(2, 3, -1, 4))

# ЗАМЫКАНИЕ

def outer(n):
    def inner(x):
        return n + x

    return inner


out1 = outer(5)
print(out1(10))

out2 = outer(6)
print(out2(4))


# def func1():
#     a = 1
#     b = "line"
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = b + "_new"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())

# def func(city):
#     count = 0
#
#     def inner():
#         nonlocal count
#         count += 1
#         print(city, count)
#
#     return inner
#
#
# res1 = func("Москва")
# res1()
# res1()
#
# res2 = func("Сочи")
# res2()
# res2()
#
# res1()

# lambda - функция (выражение)

# def func(x, y):
#     return x + y
#
#
# print(func(2, 3))
#
# print((lambda x, y, z: x + y + z)(2, 3, 4))
#
# variable = (lambda x, y: x + y)
#
# print(variable(2, 3))

# print((lambda x, y: x ** 2 + y ** 2)(2, 5))

# print((lambda a, b, c=3: a + b + c)(10, 20))

# print((lambda *args: sum(args))(1, 2, 3, 4, 5, 6))
# print((lambda *args: args)("a", "b", "c"))

# c = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4,
# )
#
# for t in c:
#     print((t("abc_")))

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# f = outer(5)
# print(f(10))
#
#
# def outer1(n):
#     return lambda x: n + x
#
#
# f1 = outer1(5)
# print(f1(10))
#
# outer2 = lambda n: lambda x: n + x
# f2 = outer2(5)
# print(f2(10))
#
# print((lambda n: lambda x: n + x)(5)(10))

# print((lambda n: lambda x: lambda y: n + x + y)(2)(4)(6))

# print((lambda n: lambda x: lambda y: n+x+y)(int(input("Введите 1 число: ")))(int(input("Введите 2 число: ")))(int(input("Введите 3 число: "))))

# d = {"b": 15, "a": 7, "c": 3}
# print(d)
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1])
# print(lst)
# print(dict(lst))