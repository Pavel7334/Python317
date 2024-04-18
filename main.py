import geometry
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

# import geometry as m
#
# # print(geometry.sqrt(4))
# # print(geometry.pi)
# print(m.ceil(3.2))
# print(m.floor(3.8))

# from geometry import pi
#
# radius = (int(input("Введите радиус окружности: ")))
# print("Длина окружности:", round(2 * pi * radius, 2))

# from geometry import sqrt
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

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# out1 = outer(5)
# print(out1(10))
#
# out2 = outer(6)
# print(out2(4))


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


# players = [
#     {'name': 'Антон', 'last_name': 'Бирюков', 'rating': 9},
#     {'name': 'Алексей', 'last_name': 'Бодня', 'rating': 10},
#     {'name': 'Федор', 'last_name': 'Сидоров', 'rating': 4},
#     {'name': 'Михаил', 'last_name': 'Семенов', 'rating': 6},
# ]
#
# res1 = sorted(players, key=lambda item: item['last_name'])
# print(res1)
# res2 = sorted(players, key=lambda item: item['rating'], reverse=True)
# print(res2)

# a = [lambda x, y: x +y, lambda x, y: x - y, lambda x, y: x * y]
# b = a[2](5,3)
# print(b)


# d = {
#     1: lambda: print("Понедельник"),
#     2: lambda: print("Вторник"),
#     3: lambda: print("Среда"),
#     4: lambda: print("Четверг"),
# }
#
# d[3]()

# print((lambda a, b: a if a > b else b)(5, 13))

# print((lambda a, b, c: a if a < b else b if b < c else c)(9, 8, 5))
# print((lambda a, b, c: a if (a < b) and (a < c) else b if (b < c) and (b < a) else c)(13, 1, 1))


# print((lambda *args: min(args))(2, 5, 8))
#
# print((lambda *args: sorted(list(args))[0])(2, 5, 8))
# print((lambda *args: sorted(list(args))[-1])(2, 5, 8))


# map(func, iterable), filter(func, iterable)

# def mult(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
#
#
# lt = list(map(mult, lst))
#
# print(lt)
#
# lt1 = list(map(lambda t: t * 2, lst))
# print(lt1)
#
# print(list(map(lambda t: t * 2, [2, 8, 12, -5, -10])))

# lst = ['1', '2', '3', '4', '5']
# print(lst)
# print(list(map(lambda x: int(x), lst)))
# print(list(map(int, lst)))


# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
# print(list(map(lambda x, y: {x: y}, st, num)))
#
# st = [5, 2, 2, 3, 9]
# num = [1, 2, 3, 4, 5]
# print(list(map(lambda x, y: x + y, st, num)))


# t = ('abcd', 'abc', 'cdefg', 'ght', 'gth')

# t2 = tuple(filter(lambda s: len(s) == 3, t))
# t2 = tuple(filter(lambda s: s * 3, t))
#
# print(t2)

# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
#
# print(list(filter(lambda s: s > 75, b)))


# from random import randint
# arr = [randint(10, 20) for i in range(11)]
# print(list(filter(lambda a: a > 10, arr)))

#

# print(list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(1, 10)))))

# print([x ** 2 for x in range(1, 10) if x % 2])


# Декораторы

# def hello():
#     return 'Hello, I am func "hello"'
#
#
# def super_func(func):
#     print('Hello, I am func "super_func"')
#     print(func())
#
#
# super_func(hello)

# def hello():
#     return 'Hello, I am func "hello"'
#
# test = hello
# print(test())
# print(id(test))
# print(id(hello))


# def my_decorator(func):
#     def inner():
#         print('Code before')
#         func()
#         print('Code after')
#
#     return inner
#
#
# def func_test():
#     print('Hello, I am func "func_test"')
#
#
# test = my_decorator(func_test)
# test()

# def my_decorator(func):  # декорирующая функция
#     def inner():
#         print('Code before')
#         func()
#         print('Code after')
#
#     return inner
#
#
# @my_decorator   # декоратор
# def func_test():    # декорируемая функция
#     print('Hello, I am func "func_test"')
#
#
# func_test()

# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @italic
# @bold
# def hello():
#     return "text"
#
#
# print(hello())


# def cnt(fn):
#     num = 0
#
#     def wrap():
#         nonlocal num
#         num += 1
#         fn()
#         print("Вызов функции: ", num)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()

# def args_decorator(fn):
#     def wrap(first, last):
#         print("Данные:", first, last)
#         fn(first, last)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print("Меня зовут ", first, last)
#
#
# print_full_name("Ирина", "Мумладзе")


# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print("args:", args)
#         print("kwargs:", kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decorator
# def func(a, b, c, study="Python"):
#     print(a, b, c, "изучают", study, end="\n\n")
#
#
# func("Борис", "Елизавета", "Светлана", study="JavaScript")
# func("Владимир", "Екатерина", "Виктор")

# def decor_args(arg1, arg2):
#     def decor(fn):
#         def wrap(x, y):
#             print(arg1, x, arg2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#
#     return decor
#
#
# @decor_args("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#
#
# summa(5, 2)
#
#
# @decor_args("Разность:", "-")
# def summa(a, b):
#     print(a - b)
#
#
# summa(5, 2)


# def decor_args(arg1):
#     def decor(fn):
#         def wrap(x):
#             return f"Результат: = {arg1 * fn(x)}"
#
#         return wrap
#
#     return decor
#
#
# @decor_args(3)
# def return_num(num):
#     return num
#
#
# print(return_num(5))


# СТРОКИ

# print(int("19"))
# print(int("19.5"))
# print(int(19.5))

# print(int("100", 2))
# print(int("100", 8))
# print(int("100", 10))
# print(int("100", 16))

# print(bin(18))  # 0b10010 - двоичная
# print(oct(18))  # 0o22 - восьмеричная
# print(hex(18))  # 0x12 - шестнадцатеричная
#
# print(0b10010)
# print(0o22)
# print(0x12)
# print(0b10010 + 0x12)

#
# q = 'Pyt'
# w = "hon"
# e = q + w
# print(e)
# print(e * 2)
# print("y1" in e)
# print(e[0])
# print(e[1:3])

# s = "Python"
# # s[3]= "t"
# s = s[:3] + 't' + s[4:]
# print(s)

# def changeCharToStr(s, old, new):
#     s2 = ""
#     i = 0
#
#     while i < len(s):
#         if s[i] == old:
#             s2 = s2 + new
#         else:
#             s2 = s2 + s[i]
#         i += 1
#
#     return s2
#
#
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# str2 = changeCharToStr(str1, "N", "P")
# # str2 = str1.replace("N", "P")
# print("str1 = ", str1)
# print("str2 = ", str2)
# print(str2)

#
# print("Привет")
# print(u"Привет")


# print("C:\\folder\\files.txt")
# print(r"C:\folder\files.txt")
# print(r"C:\folder\files\\"[:-1])
# print(r"C:\folder\files" + "\\")


# name = "Дмитрий"
# age = 25
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print(f"Меня зовут {name}. Мне {age} лет.")

# print(f"Число: {5 + 3}")
#
# ch = 5.26987412
#
# print(f"Число: {round(ch, 3)}")
# print(f"Число: {ch:.3f}")


# x = 10
# y = 5
#
# print(f"{x=}, {y=}")
# print(f"{x} x {y} / 2 = {x * y / 2}")


# num = 74
#
# print(f"{{{num}}}")
#
# print("C:\\\\text")

# dir_name = 'my_doc'
# file_name = "date.txt"
# print(fr"home\{dir_name}\{file_name}")


# def square(n):
#     """Принимает число n, возвращает квадрат числа n."""
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)


# from geometry import pi
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)


# while True:
#     n = input("-> ")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break


# s = "Test string for me"
# arr = [ord(x) for x in s]
# print("ASCII кода:", arr)
# print("Среднее арифметическое", [int(sum(arr) / len(arr))] + arr)
# arr += [ord(x) for x in input("-> ")[:3] if ord(x) not in arr]
# print(arr)
# print(arr.count(arr[-1]) -1)
#
# arr.sort(reverse=True)
# print(arr)

#
# print(chr(97))      # chr Возвращает сам букву из цифр
# print(chr(943747))

# a = 97
# b = 122
#
# if a < b:
#     a, b = b, a
#
# for i in range(b, a + 1):
#     print(chr(i), end=" ")


# print("apple" == "Apple")
# print("apple" > "Apple")


# from random import randint
#
# shortest = 7
# longest = 10
# min_ascii = 33
# max_ascii = 126
#
#
# def random_password():
#     res = ""
#     for i in range(randint(shortest, longest)):
#         rand_char = chr(randint(min_ascii, max_ascii))
#         res += rand_char
#     return res
#
#
# print("Ваш случайный пароль:", random_password())


# s = "hello, WORLD! I am learning Python."
# print(s.capitalize())   # Выводит первый символ в верхнем регистре, остальные в нижнем
# print(s.lower())   # выводит всё в нижнем регистре
# print(s.upper())   # выводит всё в верхнем регистре
# print(s.swapcase())   # HELLO, world! i AM LEARNING pYTHON.
# print(s.title())   # Hello, World! I Am Learning Python.
#
# print(s.count("h"))  # посчитает сколько букв "h" в строке
# print(s.count("h", 3))  # посчитает сколько букв "h" в строке
# print(s.count("h",3, 10))  # посчитает сколько букв "h" в строке
#
# print(s.find("Python"))  # возвращает индекс первое вхождение подстроки в строку, если такой подстроки нет возвращает -1
# print(s.find("l", 4, 20))
# print(s.find("l"))
# print(s.rfind("l"))
#
# print(s.index("l"))
# print(s.rindex("l"))


# st = input("Введите два слова через пробел: ")
# first = st[:st.find(" ")]
# second = st[st.find(" ") + 1:]
# print(second + first)


# s = "hello, WORLD! I am learning Python."
# print(s.startswith("I am", 14))
# print(s.index("I am"))
# print(s.endswith("on."))

# print(int("789"))

# print('123'.isdigit())  # проверка на наличие только числа
# print('qqwee'.isalpha())  # проверяет строку на буквы
#
# print('abc123'.isalnum())  # проверка на числа и буквы
#
# print('abc'.islower())  # находятся ли в нижнем регистре
# print('abc'.isupper())  # находятся ли в верхнем регистре
#
# n = input("Введите число: ")
# if n.isdigit():
#     n = int(n)
#     print(n * 2)

# print('py'.center(10))
# print(' py '.center(10, "-"))

# print('     py'.lstrip())  # удаляет по дефолту пробелы
# print('     py     '.rstrip())
# print('     py     '.strip())


# print('https://www.pythons.org'.strip('/:pths.org'))
# print('https://www.pythons.org'.lstrip('/:pths').rstrip('.org'))


# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# print(str1.replace("Nython", "Python"))


# s = "-"
# seq = ("a", "b", "c")
# print(s.join(seq))
#
# print("..".join(['1', '99']))
#
# print(", ".join("Hello"))


# print("Строка разделенная пробелами".split())  # ['Строка', 'разделенная', 'пробелами']
# print('www.python.org.ru'.split(".", 2))
# print('www.python.org.ru'.rsplit(".", 2))


# a = input("-> ").split()    # ['Hello', 'world']
# b = list(map(int, a))
# print(b)

import re

# s = "Я ищу совпадение в 2024 году. И я их найду в 2 счёта."
# reg = "а"

# print(re.findall(reg, s))   # возвращает список содержащий все совпадения
#
# print(re.search(reg, s))    # месторасположение первого совпадения с объектом
# print(re.search(reg, s).span())    # месторасположение первого совпадения с объектом
# print(re.search(reg, s).start())    # месторасположение первого совпадения с объектом
# print(re.search(reg, s).end())    # месторасположение первого совпадения с объектом
# print(re.search(reg, s).group())    # месторасположение первого совпадения с объектом
#
# print(re.match(reg, s))     # поиск совпадения с шаблоном вначале строки
#
# print(re.split(reg, s, 1))     # возвращает список, в котором строка разбита по шаблону
#
# print(re.sub(reg, "!", s, 2))   # поиск и замена


# s = "Я ищу совпадение в 2024 году. И я их найду в 2 счёта. 198673 Hello"
# reg = "[21][0-9][0-9][0-9]"   # для поиска года
# reg = "[0-9]"
# reg = "[А-яЁё]"
# reg = "[A-Za-z]"
# reg = "\\."  # для экранирования точет
# reg = r"\."  # для экранирования точет
# reg = r"[A-Za-z\[\]-]"
# reg = f"[^0-9]"     # выводи всё кроме того что в скобках ^ - циркумфлекс
# reg = f"[]"
# print(re.findall(reg, s))


# st = "Час в 24-часовом формате от 00 до 23. 2021-06-15Т21:45. Минуты, в диапазоне от 00 до 59. 2021-06-15Т01:09."
# reg = "[0-2][0-9]:[0-5][0-9]"
# print(re.findall(reg, st, 2))

# s = "Я ищу совпадение в 2024 году. И я их найду в 2 счёта. 198673 Hello"
# reg = r"20*"
# print(re.findall(reg, s))

# Кол-во повторений
# + - от 1 до бесконечности
# * - от 1 до бесконечности
# ? - 0 до 1

# d = "Цифры: 7, +17, -42, 0013, 0.3"
# reg = r'[+-]?[\d.]+'
# print(re.findall(reg, d))


# s = "05-03-1987 # Дата рождения"
# print("Дата рождения:", re.sub(r"\s#.*", "", s))
# print("Дата рождения", re.sub("-", ".", re.sub("\\s#.*", "", s)))
# print(re.sub('-', '.', s))
# Дата рождения: 05.03.1987

# s = "author=Пушкин А.С.; title  = Евгений Онегин; price =200; year= 1831"
# reg = r'\w+\s*=\s*[^;]+'
# # reg = r'[^;]+'
# print(re.findall(reg, s))

# s = "12 сентября 2024 года"
# reg = r"\d{4}"              # {} что бы цифр было подряд 4
# print(re.findall(reg, s))


# def validate_login(login):
#     return re.findall(r"^[A-Za-z0-9-]{3,16}", login)
#
#
# print(validate_login("Python-master"))

# print(re.findall(r"\w+", "12 + й"))
# print(re.findall(r"\w+", "12 + й", flags=re.ASCII))

# text = "Hello world"
# print(re.findall(r"\w\+", text, re.DEBUG))

# s = "Я ищу совпадение в 2024 году. И я их найду в 2 счёта."
# reg = "я"
#
# print(re.findall(reg, s, re.IGNORECASE))
# print(re.findall(reg, s, re.I))


# text = """
# one
# two
# """
#
# print(re.findall(r"one.\w+", text))
# print(re.findall(r"one.\w+", text, re.DOTALL))


# print(re.findall(r"one$", text))
# print(re.findall(r"one$", text, re.MULTILINE))


# print(re.findall('''
# [A-Za-z0-9._-] +  # part 1
# @                 # @
# [A-Za-z.-]+       # part 2
# ''', 'test@mail.ru', re.VERBOSE))

# text = """Python,
# python,
# PYTHON"""
# reg = "(?im)^python"
# print(re.findall(reg, text))

# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall("<.*?>", text))

# s = "Ольга и Виталий отично учатся!"
#
# reg = "Петр|Ольга|Виталий"  # | или
# print(re.findall(reg, s))

# s = "int = 4, float = 4.0f, double = 8.0"
# # reg = r"\w+\s*=\s*\d[.\w]*"
# # reg = r"(?:int|float)\s*=\s*\d[.\w]*"
# reg = r"(int|float)\s*=\s*(\d[.\w]*)"
# print(re.findall(reg, s))
# print(re.search(reg, s))

# (?: ....) - группирующая скобка не является сохраняющей

# s = "5 + 7*2 - 4"
# reg = r"\s*([+*-])\s*"
# print(re.split(reg, s))


# s = "01-12-2024"
# reg = "(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-([0-9][0-9][0-9][0-9])"
# print(re.findall(reg, s))
# print(re.search(reg, s).group())
# m = re.search(reg, s)
# print(m[0])
# print(m[1])
# print(m[2])
# print(m[3])
# print(re.search(reg, s).group())
# print(re.search(reg, s).group(1))
# print(re.search(reg, s).group(2))
# print(re.search(reg, s).group(3))

# text = """
# Самара
# Москва
# Тверь
# Уфа
# Казань
# """
#
# count = 0
#
#
# def replace_find(m):
#     global count
#     count += 1
#     return f"<option value='{count}'>{m.group(1)}</option>\n"
#
#
# print(re.sub(r"\s*(\w+)\s*", replace_find, text))

# s = "Самолет прилетает 10/23/2024. Будем рады вас видеть после 10/24/2024."  # 23.10.2024    24.10.2024
# reg = r"(\d{2})/(\d{2})/(\d{4})"
# print(re.sub(reg, r"\2.\1.\3", s))

# s = "yandex.com and yandex.ru"
# reg = r"([a-z0-9-]{2,}\.[a-z]{2,4})"
# print(re.sub(reg, r"http://\1", s))


# Рекурсия

# def elevator(n):
#     if n == 0:
#         print("Вы в подвале")
#         return
#     print("=>", n)
#     elevator(n-1)
#     print(n, end=" ")
#
#
# n1 = int(input("На каком вы этаже: "))
# elevator(n1)


# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res

# def sum_list(lst):
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         return lst[0] + sum_list(lst[1:])
#
#
# print(sum_list([1, 3, 5, 7, 9]))
#
#
# def func(n):
#     return n * 2
#
#
# print(func(5))


# def to_str(n, base):
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base]
#
#
# print(to_str(254, 10))   # to_str(254, 16) => FE

#                                         РЕКУРСИЯ С ВЛОЖЕННЫМИ СПИСКАМИ
# names = ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
#
#
# def count_items(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
#
#
# print(count_items(names))


# def remove(text):
#     if not text:
#         return ""
#     if text[0] == "\n" or text[0] == " ":
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])
#
#
# print(remove("  Hello\nWorld "))


#                                                   ФАЙЛЫ

# f = open("test.txt", "r")
# # f = open(r"F:\КУРС ТОП АКАДЕМИЯ\python317\test.txt", "r")
# print(f.read(3))
# print(f.read())           # возвращает весь документ
# # print(f)
# # print(*f)
# # print(f.mode)
# # print(f.name)
# # print(f.encoding)
# f.close()
# # print(f.closed)


# f = open("test2.txt", "r")
# print(f.readline())       # возвращает 1 строку
# print(f.readline(8))
# print(f.readline())
# f.close()


# f = open("test2.txt", "r")
# print(f.readlines(26))
# print(f.readlines())      # возвращает список строк
# f.close()

# print(len(f.readlines()))
# f = open("test2.txt", "r")
# count = 0
# for line in f:
#     print(line, end="")
#     count += 1
# f.close()
# print(count)

# f = open("xyz.txt", "w")
# f.write("Hello\nWorld\n")
# f.close()

# f = open("xyz.txt", "a")
# f.write("New text.\n")
# f.close()

# f = open("xyz.txt", "a")
# lines = ['\nThis is line 1', '\nThis is line 2']
# f.writelines(lines)
# f.close()

# f = open("xyz.txt", "w")
# lst = [str(i) + " " for i in range(1, 20)]
# print(lst)
# for index in lst:
#     f.write(index + "\t")
# f.writelines(lst)
# f.close()

# f = open("test3.txt", "w")
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл\n")
# f.close()

# f = open('test3.txt', 'r')
# read_file = f.readlines()
# print(read_file)
# read_file[1] = "Hello world!\n"
# print(read_file)
# f.close()
#
# f = open("test3.txt", "w")
# f.writelines(read_file)
# f.close()

# f = open("test3.txt", 'r')
# read_file = f.readlines()
# pos = int(input("Введите индекс строки для удаления: "))
# if 0 < pos < len(read_file):
#     del_pos = read_file.pop(pos)
# else:
#     print("Индекс введен неверно")
# f.close()
#
# f = open("test3.txt", 'w')
# f.writelines(read_file)
# f.close()

# f = open("test.txt", "r")
# print(f.read(3))
# print(f.tell())     # возвращает текущую позицию условного курсора в файле
# print(f.seek(1))    # перемещает условный курсор в заданную позицию
# print(f.read())
# print(f.tell())
# f.close()

# f = open("test.txt", "r+")
# print(f.write("I am learning Python"))
# print(f.seek(3))
# print(f.write("-new string-"))
# print(f.tell())
# f.close()

# f = open("test2.txt", "a+")
# # print(f.write("111111I am learning Python"))
# print(f.read())
# f.close()


# with open("test2.txt", 'w+') as f:
#     print(f.write('01234\n56789'))
# print(f.closed)

# with open("test2.txt", 'r') as f:
#     for line in f:
#         print(line[:3])


# file_name = "res.txt"
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
# print(str(lst))
#
#
# def get_line(lt):
#     lt = map(str, lt)
#     return ' '.join(lt)
#
#
# with open(file_name, 'w') as f:
#     f.write(get_line(lst))
#
# with open(file_name, 'r') as f:
#     st = f.read()
#
# print(st)
# print(type(st))
#
# nums = list(map(float, st.split()))
# print(nums)
# print(type(nums[0]))


# def longest_worlds(file):
#     with open(file, 'r', encoding="utf-8") as text:
#         w = text.read().split()
#         print(w)
#         max_length = len(max(w, key=len))
#         print(max_length)
#         res = [i for i in w if len(i) == max_length]
#         if len(res) == 1:
#             return res[0]
#         return res
#
#
# print(longest_worlds('test.txt'))

# f = open("test2.txt", "wb")
# print(f.write("1111 I am learning Python 1111"))
# f.close()


# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n"
#
# with open('one.txt', 'w') as f:
#     f.write(text)


# with open('one.txt', 'r') as fr, open('two.txt', 'w') as fw:
#     for line in fr:
#         line = line.replace("Строка", "Линия -")
#         fw.write(line)


#                                             Модуль OS, os.path

import os

# import os.path

# print(os.path.split(r"F:\КУРС ТОП АКАДЕМИЯ\python317\nested1\nested2\nested3\nested4\two.txt"))
# print(os.getcwd())   # Возвращает текущую директорию
# print(os.listdir())  # Возвращает список директорий и файлов
# print(os.listdir(".."))

# os.mkdir("folder1")  # создаёт папку
# os.makedirs("nested1/nested2/nested3")  # создаёт вложенные папки

# os.rmdir("folder1")    # удаляет пустую папку
# os.rmdir("nested1/nested2/nested3")

# os.remove("xyz.txt")    # удаляет файл

# os.rename("test.txt", "new.txt")  # переименование файла и можно папки

# os.rename("test.txt",
#           "nested1/nested3/two.txt")  # переименование файла и папки, перемещает документы, создавая промежуточную директорию

# for root, dirs, files in os.walk("nested1"):
#     print("Root:", root)
#     print("\tSubdirs:", dirs)
#     print("\t\tFiles:", files)


# def remove_empty_dirs(root_tree):
#     print(f"Удаление пустых директив в ветви {root_tree}")
#     print('-' * 50)
#     for root, dirs, files in os.walk(root_tree):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f"Директория {root} удалена.")
#     print('-' * 50)
#
#
# remove_empty_dirs("nested1")

# print(os.path.split(r"F:\КУРС ТОП АКАДЕМИЯ\\\\nested3\nested4\two.txt"))     # [1]
#
# print(os.path.join(r'F:\КУРС ТОП АКАДЕМИЯ', 'python317', 'nested1', 'nested2', 'two.txt'))

# dirs = [r'Work\F1', r'Work\F2\F21']
#
# for d in dirs:
#     os.makedirs(d)


# files = {
#     'Work': ['w.txt'],
#     r'Work\F1': ['f11.txt', 'f12.txt', 'f12.txt'],
#     r'Work\F2\F21': ['f211.txt', 'f212.txt']
# }
#
# for dir1, files in files.items():
#     for file in files:
#         file_path = os.path.join(dir1, file)
#         open(file_path, 'w').close()
#
# file_with_text = [r'Work\w.txt', r'Work\F1\f12.txt', r'Work\F2\F21\f211.txt', r'Work\F2\F21\f212.txt']
#
# for file in file_with_text:
#     with open(file, 'w') as f:
#         f.write(f"Текст в файлу {file}")

# Work\w.txt
# Work\F1\f11.txt
# Work\F1\f12.txt
# Work\F1\f12.txt
# Work\F2\F21\f211.txt
# Work\F2\F21\f212.txt

# print(os.path.exists(r'nested1\nested2'))   # проверка на существование пути
# print(os.path.getsize('main.py'))           # размер документа в байтах

# import time
#
# path = "main.py"
#
# print(os.path.getctime(path))   # возвращает время создания файла
# print(os.path.getatime(path))   # возвращает время последнего доступа к файлу
# print(os.path.getmtime(path))   # возвращает время последнего изменения файла (в секунду)
#
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(os.path.getctime(path))))
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(os.path.getatime(path))))
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(os.path.getmtime(path))))


#                                                 ООП


# class Point:
#     """Класс для предоставления координат на плоскости"""
#     x = 1
#     y = 1
#
#
# p1 = Point()
# print(p1.x)
# print(Point.x)
# print(type(p1))
# print(Point.__doc__)
# print(Point.__name__)
# print(dir(Point))


# class Point:
#     """Класс для предоставления координат на плоскости"""
#     x = 1
#     y = 1
#
#
# p1 = Point()
# p1.x = 10
# p1.y = 20
# p1.z = 30
# print(p1.x, p1.y)
# print(p1.__dict__)
#
# p2 = Point()
# print(p2.x, p2.y)


# class Point:
#     x = 1
#     y = 1
#
#     def set_coord(self, a, b):
#         self.x = a
#         self.y = b
#         print(self.__dict__)
#
#
# p1 = Point()
# # p1.x = 5
# # p1.y = 10
# p1.set_coord(5, 10)
# # Point.set_coord(p1)
#
# p2 = Point()
#
# # p2.x = 50
# # p2.y = 100
# p2.set_coord(50, 100)

# class Human:
#     name = "name"
#     birthday = "00.00.0000"
#     phone = "00-00-00"
#     country = "country"
#     city = "city"
#     address = "street, house"
#
#     def print_info(self):
#         print(" Персональные данну ".center(40, "*"))
#         print(
#             f"Имя: {self.name}\nДата рождения: {self.birthday}\nНомер телефона: {self.phone}\nСтрана: {self.country}\n"
#             f"Город: {self.city}\nДомашний адрес: {self.address}")
#         print("=" * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):  # установить имя
#         self.name = name
#
#     def get_name(self):  # получить имя
#         return self.name
#
#     def set_birthday(self, birthday):
#         self.birthday = birthday
#
#     def get_birthday(self):
#         return self.birthday
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва", "Чистопрудный бульвар 1A")
# h1.print_info()
# h1.set_name("Юлия")
# print(h1.get_name())
# h1.set_birthday("23.12.1990")
# print(h1.get_birthday())
# h1.print_info()


# class Person:
#     skill = 10  # статическое
#     count = 0
#
#     def __init__(self, name, surname):  # Инициализатор
#         self.name = name  # динамическое
#         self.surname = surname
#         # print("Инициализатор")
#         # Person.count += 1
#
#     # def __del__(self):  # финализатор либо деструктор
#     #     print("Удаление экземпляра:", self.__class__.__name__)
#
#     def print_info(self):
#         print("Данные сотрудника:", self.name, self.surname)
#
#     # def add_skill(self, k):
#     #     self.skill += k
#     #     print("Квалификация сотрудника: ", self.skill, end="\n\n")
#
#
# p1 = Person("Виктор", "Резник")
# p1.print_info()
# # p1.add_skill(3)
# # del p1
# # print(p1.count)
#
# p2 = Person("Анна", "Долгих")
# p2.print_info()
# # p2.add_skill(2)
# # print(p1.count)
# # print(p2.count)
# # print(Person.count)
#
# p3 = Person("Анна", "Долгих")
# # print(p1.count)
# # print(p2.count)
# # print(Person.count)


# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Инициализация робота:", self.name)
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, "выключается!")
#         Robot.k -= 1
#
#         if Robot.k == 0:
#             print(self.name, "был последним")
#         else:
#             print("Работающих роботов осталось:", Robot.k)
#
#     def say_hi(self):
#         print("Приветствую! Меня зовут:", self.name)
#
#
# droid1 = Robot('R2 - D2')
# droid1.say_hi()
# print("Численность роботов:", Robot.k)
# print()
# droid2 = Robot('C - 3PO')  # перемещение местами строк shift + alt + стрелка вниз или вверх
# droid2.say_hi()
# print("Численность роботов:", Robot.k)
# print("\nЗдесь роботы могут проделать какую-то работу\n")
# print("Роботы закончили свою работу. Давайте их выключим")
# del droid1
# del droid2
# print("Численность роботов:", Robot.k)

# class Point:
#     def __init__(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x  # _Point__x
#             self.__y = y  # _Point__y
#
#     def __check_value(a):
#         if isinstance(a, int) or isinstance(a, float):
#             return True
#         return False
#
#     def set_coord(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coord(self):
#         return self.__x, self.__y
#
#     def set_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координата Х должны быть числом")
#
#     def set_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print("Координата Y должны быть числом")
#
#     def get_x(self):
#         return self.__x
#
#
# p1 = Point(5, 10)
# print(p1.get_coord())
# p1.set_coord(100.5, 200.3)
# print(p1.get_coord())
# print(p1._Point__x, p1._Point__y)
# p1.set_x(50)
# print(p1.get_x())
# p1._Point__x = 111
# print(p1.__dict__)
# print(p1._Point__x)
# print(Point.__dict__)


# Модификаторы доступа:
# public - self.name
# protected - self._name
# private - self.__name


# class Rectangle:
#
#     __slots__ = ["__length", "__width"]
#
#     def __init__(self, length, width):
#         self.__length = length
#         self.__width = width
#
#     def __check_value(a):
#         if isinstance(a, int) or isinstance(a, float):
#             return True
#         return False
#
#     def set_length(self, length):
#         if Rectangle.__check_value(length):
#             self.__length = length
#
#     def set_width(self, width):
#         if Rectangle.__check_value(width):
#             self.__width = width
#
#     def get_width(self):
#         return self.__width
#
#     def get_length(self):
#         return self.__length
#
#     def get_area(self):
#         return self.__length * self.__width
#
#     def get_perimetr(self):
#         return 2 * (self.__length + self.__width)
#
#     def get_hypotenuse(self):
#         return round(geometry.sqrt(self.__length ** 2 + self.__width ** 2), 2)
#
#     def get_draw(self):
#         print(("*" * self.__width + "\n") * self.__length)
#
#
# rect = Rectangle(4, 12)
# rect.set_length(4)
# rect.set_width(12)
# print("Длина прямоугольника:", rect.get_length())
# print("Ширина прямоугольника:", rect.get_width())
# print("Площадь прямоугольника:", rect.get_area())
# print("Периметр прямоугольника:", rect.get_perimetr())
# print("Гипотенуза прямоугольника:", rect.get_hypotenuse())
# rect.get_draw()
# rect.x = 20
# print(rect.x)
# print(rect.__dict__)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __set_x(self, x):
#         self.__x = x
#         print("Сеттер")
#
#     def __get_x(self):
#         print("Геттер")
#         return self.__x
#
#     def __del_x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.x = 100
# print(p1.x)
# del p1.x
# print(p1.__dict__)

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __check_value(a):
#         if isinstance(a, int) or isinstance(a, float):
#             return True
#         return False
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#
#     @x.deleter
#     def x(self):
#         del self.__x
#
#     # x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.x = 100
# print(p1.x)
# del p1.x
# print(p1.__dict__)


# class KgToPounds:
#
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print("Килограммы задаются только числами")
#
#     def to_pound(self):
#         return self.__kg * 2.205
#
#
# weight = KgToPounds(12)
# print(weight.kg, "кг =>", weight.to_pound(), "фунтов")
# weight.kg = 41
# print(weight.kg, "кг =>", weight.to_pound(), "фунтов")
# weight.kg = "два"

# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
# p4 = Point()
# p5 = Point()
# print(Point.get_count())


# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# print(Change.inc(10), Change.dec(10))


# class Fact:
#
#     @staticmethod
#     def max(*args):
#         return max(args)
#
#     @staticmethod
#     def min(*args):
#         return min(args)
#
#     @staticmethod
#     def fact(args):
#         factor = 1
#         for i in range(1, args + 1):
#             factor *= i
#         return factor
#
#     @staticmethod
#     def avg(*args):
#         return sum(args) / len(args)
#
#
# print(Fact.max(3, 5, 7, 9))
# print(Fact.min(3, 5, 7, 9))
# print(Fact.fact(5))
# print(Fact.avg(3, 5, 7, 9))


# class Date:
#
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, string_date):
#         day, month, year = map(int, string_date.split("."))
#         return cls(day, month, year)
#
#     @staticmethod
#     def is_date_valid(date_as_string):
#         if date_as_string.count('.') == 2:
#             day, month, year = map(int, date_as_string.split("."))
#             return day <= 31 and month <= 12 and year <= 3999
#
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"
#
#
# dates = [
#     "15.12.2024",
#     "23-10-2023",
#     "01.01.2021",
#     "12.31.2020",
# ]
#
# for d in dates:
#     if Date.is_date_valid(d):
#         date = Date.from_string(d)
#         print(date.string_to_db())
#     else:
#         print("Некорректная дата")
#
# date2 = Date.from_string("23.10.2023")
# print(date2.string_to_db())
# date3 = Date.from_string("15.12.2024")
# print(date3.string_to_db())

# day, month, year = map(int, string_date.split("."))
# date = Date(day, month, year)
# print(date.string_to_db())


# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, surname, num, percent, value):
#         self.surname = surname
#         self.num = num
#         self.percent = percent
#         self.value = value
#         print(f"Счет #{self.num} принадлежащий {self.surname} был открыт.")
#         print("*" * 50)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет #{self.num} принадлежащий {self.surname} был закрыт.")
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#
#     def convert_to_usd(self):
#         usd = Account.convert(self.value, Account.rate_usd)
#         print(f"Состояние счета: {usd} {Account.suffix_usd}")
#
#     def convert_to_eur(self):
#         eur = Account.convert(self.value, Account.rate_eur)
#         print(f"Состояние счета: {eur} {Account.suffix_eur}")
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_percent(self):
#         self.value += self.value * self.percent
#         print(f"Проценты были успешно начислены!")
#         self.print_balance()
#
#     def withdraw_money(self, value):
#         if value > self.value:
#             print(f"К сожалению у вас нет {value} {Account.suffix}")
#         else:
#             self.value -= value
#             print(f"{value} {Account.suffix} было успешно снято с вашего счета.")
#         self.print_balance()
#
#     def add_money(self, value):
#         self.value += value
#         print(f"{value} {Account.suffix} было успешно добавлено на ваш счет.")
#         self.print_balance()
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.suffix}:")
#
#     def print_info(self):
#         print("Информация о счёте")
#         print("-" * 20)
#         print(f"#{self.num}")
#         print(f"Владелец: {self.surname}")
#         self.print_balance()
#         print(f"Проценты: {self.percent:.0%}")
#         print("-" * 20)
#
#
# acc = Account("Долгих", "12345", 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
#
# Account.set_usd_rate(2)
# acc.convert_to_usd()
# Account.set_eur_rate(3)
# acc.convert_to_eur()
# print()
#
# acc.edit_owner("Дюма")
# acc.print_info()
# print()
#
# acc.add_percent()
# print()
#
# acc.withdraw_money(3000)
# print()
#
# acc.withdraw_money(100)
# print()
#
# acc.add_money(5000)
# print()
#
# acc.withdraw_money(3000)
# print()


# class UserData:
#     def __init__(self, fio, old, ps, weight):
#         self.fio = fio
#         self.old = old
#         self.password = ps
#         self.weight = weight
#
#     @staticmethod
#     def varify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()
#         if len(f) != 3:
#             raise ValueError("ФИО должно быть состоять из трех слов")
#         letters = "".join(re.findall("[a-zа-яё-]", fio, re.IGNORECASE))
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise ValueError("В ФИО можно использовать только буквы и дефис")
#
#     @staticmethod
#     def verify_old(old):
#         if not isinstance(old, int) or old < 14 or old > 120:
#             raise TypeError("Возраст должен быть целым числом в диапазоне от 14 до 120")
#
#     @staticmethod
#     def verify_weight(weight):
#         if not isinstance(weight, float) or weight < 30:
#             raise TypeError("Вес должен быть вещественным числом от 30 кг и выше")
#
#     @staticmethod
#     def verify_password(ps):
#         if not isinstance(ps, str) or len(ps) < 8:
#             raise TypeError("Пароль должен быть строкой не менее 8 символов")
#         s = ps.split()
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise ValueError("Неверный формат паспорта")
#         for p in s:
#             if not p.isdigit():
#                 raise TypeError("Серия и номер паспорта должны содержать только цифры")
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, value):
#         self.varify_fio(value)
#         self.__fio = value
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, year):
#         self.verify_old(year)
#         self.__old = year
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, value):
#         self.verify_weight(value)
#         self.__weight = value
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, value):
#         self.verify_password(value)
#         self.__password = value
#
#
# p1 = UserData("Волков Игорь Николаевич", 24, "1234 567890", 80.8)
#
# p1.fio = "Соболев Игорь Николаевич"
# print(p1.__dict__)


# class Point:
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self.__width = width
#
#     def get_width(self):
#         return self.__width
#
#
# class Line(Prop):
#
#     def __init__(self, *args):
#         super().__init__(*args)
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self.get_width()}")
#         # return f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self.get_width()}"
#
#
# class Rect(Prop):
#
#     def draw_line(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self.get_width()}")
#         # return f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self.get_width()}"
#
#
# line = Line(Point(1, 2), Point(10, 20), "yellow", 5)
# line.draw_line()
# # print(line._color)
# rect = Rect(Point(30, 40), Point(70, 80))
# rect.draw_line()
# print(issubclass(Line, Prop))

# class Figure:
#
#     def __init__(self, color):
#         self.color = color
#
#
# class Rectangle(Figure):
#
#     def __init__(self, width, height, color):
#         super().__init__(color)
#         self.__width = width
#         self.__height = height
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, value):
#         if value > 0:
#             self.__width = value
#         else:
#             raise ValueError("Ширина прямоугольника должна быть больше нуля")
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, value):
#         if value > 0:
#             self.__height = value
#         else:
#             raise ValueError("Высота прямоугольника должна быть больше нуля")
#
#     def area(self):
#         print(f"Площадь {self.color} прямоугольника:", end=" ")
#         return self.__width * self.__height
#
#
# rect = Rectangle(10, 20, "green")
# print(rect.color)
# print(rect.area())

# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f"Прямоугольник:\nШирина: {self.width}\nВысота: {self.height}")
#
#
# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         super().__init__(width, height)
#         self.fon = background
#
#     def show_rect(self):
#         super().show_rect()
#         print("Фон:", self.fon)
#
#
# class RectBorder(Rect):
#     def __init__(self, width, height, px, solid, red):
#         super().__init__(width, height)
#         self.px = px
#         self.solid = solid
#         self.red = red
#
#     def show_rect(self):
#         super().show_rect()
#         print(f"Рамка: {self.px} {self.solid} {self.red}")
#
#
# shape1 = RectFon(400, 200, "yellow")
# shape1.show_rect()
# print()
# shape2 = RectBorder(400, 200, 5, "solid", "red")
# shape2.show_rect()

# class Vector(list):
#     def __str__(self):
#         return " ".join(map(str, self))
#
#
# v = Vector([1, 2, 3])
# print(v)

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#
# class Line(Prop):
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def set_coord(self, sp: Point = None, ep: Point = None):
#         if ep is None:
#             self._sp = sp
#         elif sp is None:
#             self._ep = ep
#         else:
#             self._sp = sp
#             self._ep = ep
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coord(Point(12, 18), Point(100, 200))
# line.draw_line()
# line.set_coord(Point(-10, -20))
# line.draw_line()
#
# line.set_coord(ep=Point(500, 700))
# line.draw_line()


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def draw(self):
#         raise NotImplementedError("В дочернем классе должен быть метод draw()")
#
#
# class Line(Prop):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Rect(Prop):
#     def draw(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Ellipse(Prop):
#     def draw(self):
#         print(f"Рисование эллипса: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# figs = list()
# figs.append(Line(Point(0, 0), Point(10, 10)))
# figs.append(Line(Point(10, 10), Point(20, 10)))
# figs.append(Rect(Point(50, 50), Point(100, 100)))
# figs.append(Ellipse(Point(-10, -10), Point(30, 30)))
#
# for f in figs:
#     f.draw()

#                                                        # Абстрактные методы
#                                                        # Абстрактный класс

# from abc import ABC, abstractmethod
#
#
# class Chess(ABC):  # Абстрактный класс
#
#     def draw(self):
#         print("Нарисовал шахматную фигуру")
#
#     @abstractmethod
#     def move(self):  # Абстрактный метод
#         print("Метод move() в базовом классе")
#
#
# class Queen(Chess):  # Класс-прямоугольник
#
#     def move(self):
#         super().move()
#         print("Ферзь перемещается на е2е4")
#
#
# q = Queen()
# q.draw()
# q.move()

# from geometry import pi
#
#
# class Table:
#     def __init__(self, width=None, length=None, radius=None):
#         if radius is None:
#             self._width = width
#             self._length = length
#         else:
#             self._radius = radius
#
#     def calc_area(self):
#         raise NotImplementedError("В дочернем классе должен быть метод calc_area()")
#
#
# class SqTable(Table):
#     def calc_area(self):
#         return self._width * self._length
#
#
# class RoundTable(Table):
#
#     def calc_area(self):
#         return round(pi * self._radius ** 2, 2)
#
#
# table = SqTable(20, 10)
# print(table.__dict__)
# print(table.calc_area())
#
# table = RoundTable(radius=20)
# print(table.__dict__)
# print(table.calc_area())

# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     suffix = "RUB"
#
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     @abstractmethod
#     def print_value(self):
#         print(self.value, end=" ")
#
#     def show(self):
#         print(f"= {self.convert_to_rub():.2f} {Currency.suffix}")
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = "USD"
#
#     def convert_to_rub(self):
#         return self.value * Dollar.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=" ")
#
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     suffix = "EUR"
#
#     def convert_to_rub(self):
#         return self.value * Euro.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end=" ")
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
# print("*" * 50)
# for elem in d:
#     elem.print_value()
#     elem.show()
#
# print("*" * 50)
# for elem in e:
#     elem.print_value()
#     elem.show()


#                                                       Интерфейсы

# from abc import ABC, abstractmethod
#
#
# class Father(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#     def display1(self):
#         print("Child Class")
#
#
# class GrandChild(Child):
#     def display2(self):
#         print("GrandChild Class")
#
#
# ch = GrandChild()
# ch.display1()
# ch.display2()

#                                                   Вложенные классы

# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def outer_method():
#         print("Внешний метод")
#
#     def instance_method(self):
#         print("instance_method")
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_method(self):
#             print("Внутренний метод", MyOuter.age, self.obj.name)
#             MyOuter.outer_method()
#             self.obj.instance_method()
#
#
# out = MyOuter("Внешний")
# print(out.name)
# inn = out.MyInner("Внутренний", out)
# print(inn.inner_name)
# inn.inner_method()

# class Color:
#     def __init__(self):
#         self.name = "Green"
#         self.lg = self.LightGreen()
#         self.dg = self.DarkGreen()
#
#     def show(self):
#         print("Name:", self.name)
#
#     class LightGreen:
#         def __init__(self):
#             self.name = "LightGreen"
#
#         def display(self):
#             print("Name:", self.name)
#
#     class DarkGreen:
#         def __init__(self):
#             self.name = "DarkGreen"
#
#         def display(self):
#             print("Name:", self.name)
#
#
# outer = Color()
# outer.show()
# g = outer.lg
# g.display()
# dg = outer.dg
# dg.display()
# class Computer:
#
#     def __init__(self):
#         self.name = "PC001"
#         self.os = self.OS()
#         self.cpu = self.CPU()
#
#     class OS:
#         def system(self):
#             return "Windows 10"
#
#     class CPU:
#         def make(self):
#             return "Intel"
#
#         def model(self):
#             return "Core-i7"
#
#
# comp = Computer()
# my_os = comp.os
# my_cpu = comp.cpu
# print(comp.name, my_os.system(), my_cpu.make(), my_cpu.model())

# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f"{self.__class__}: {self.name}"
#
#     def __str__(self):
#         return self.name
#
#
# cat = [Cat("Мурзик"), Cat("Пушок")]
# print(cat)

# class Point:
#
#     def __init__(self, *args):
#         self.coord = args  # tuple(1, 2)
#         self.color = "red"
#         self.width = 2
#
#     def __len__(self):
#         return len(self.coord)
#
#
# p = Point(1, 2, 3, 4)
# print(len(p.coord))

# import geometry
#
#
# class Point:
#     __slots__ = ("x", "y", '__length')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = geometry.sqrt(x * x + y * y)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# p1 = Point(10, 20)
# print(p1.x, p1.y)
# # p1.z = 30
# # print(p1.z)
# print(p1.length)

# class Point:
#     __slots__ = ("x", "y")
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# pt1 = Point(1, 2)
# pt2 = Point2(1, 2)
#
# print("pt1 =", pt1.__sizeof__())
# print("pt2 =", pt2.__sizeof__() + pt2.__dict__.__sizeof__())

# class Point:
#     __slots__ = ("x", "y")
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     __slots__ = "z"
#
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.z = z
#
#
# p = Point(1, 2)
# pt3 = Point3D(1, 2, 3)
# print(pt3.z)

# Множественное наследование

# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def slips(self):
#         print(self.name, "slips")
#
#
# class Pet(Creature):
#     def plays(self):
#         print(self.name, "plays")
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name, "barks")
#
#
# d = Dog("Бобик")
# d.bark()
# d.slips()
# d.plays()


# class A:
#     def __init__(self):
#         print("Class A")
#
#
# class B(A):
#     def __init__(self):
#         print("Class B")
#
#
# class C(A):
#     def __init__(self):
#         print("Class C")
#
#
# class D(B, C):
#     def __init__(self):
#         print("Class D")
#
#
# d = D()
# print(D.mro())


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Styles:
#     def __init__(self, color="red", width=1):
#         print("Инициализатор Styles")
#         self._color = color
#         self._width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, color="red", width=1):
#         print("Инициализатор Pos")
#         self._sp = sp
#         self._ep = ep
#         # Styles.__init__(self, color, width)
#         super().__init__(color, width)
#
#
# class Line(Pos, Styles):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# l1 = Line(Point(10, 10), Point(100, 100))
# l1.draw()

#                                                    #Миксины

# class Goods:
#     def __init__(self, name, weight, price):
#         print("Инициализатор Goods")
#         self.name = name
#         self.weight = weight
#         self.price = price
#         super().__init__()
#
#     def print_info(self):
#         print(f"{self.name}, {self.weight}, {self.price}")
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print("Инициализатор MixinLog")
#         MixinLog.ID += 1
#         self.id = MixinLog.ID
#
#     def save_sell_log(self):
#         print(f"{self.id}: товар был продан в 00:00")
#
#
# class NoteBook(Goods, MixinLog):
#     pass
#
#
# n = NoteBook("HP", 1.5, 35000)
# n.print_info()
# n.save_sell_log()


#                                                    # Перегрузка методов

# 24 * 60 * 60 = 86400 - число секунд  в одном дне


# class Clock:
#     __DAY = 86400
#
#     def __init__(self, seconds: int):
#         if not isinstance(seconds, int):
#             raise TypeError("Секунды должны быть целым числом")
#         self.seconds = seconds % self.__DAY
#
#     def get_format_time(self):
#         s = self.seconds % 60
#         m = (self.seconds // 60) % 60
#         h = (self.seconds // 3600) % 24
#         return f"{Clock.__get_formatted_num(h)}:{Clock.__get_formatted_num(m)}:{Clock.__get_formatted_num(s)}"
#
#     @staticmethod
#     def __get_formatted_num(num):
#         return str(num) if num > 9 else f"0{num}"
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.seconds + other.seconds)
#
#     def __eq__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         if self.seconds == other.seconds:
#             return True
#         return False
#
#     def __ne__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         if self.seconds != other.seconds:
#             return True
#         return False
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise TypeError("Ключ должен быть типом str")
#         if item == "hour":
#             return (self.seconds // 3600) % 24
#         if item == "minute":
#             return (self.seconds // 60) % 60
#         if item == "second":
#             return self.seconds % 60
#         return "Неверный ключ"
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise TypeError("Ключ должен быть типом str")
#         if not isinstance(value, int):
#             raise TypeError("Значение должно быть целым числом")
#
#         s = self.seconds % 60
#         m = (self.seconds // 60) % 60
#         h = (self.seconds // 3600) % 24
#
#         if key == "hour":
#             self.seconds = s + 60 * m + value * 3600
#         if key == "minute":
#             self.seconds = s + 60 * value + h * 3600
#         if key == "second":
#             self.seconds = value + 60 * m + h * 3600
#
#
# c1 = Clock(80000)
# print(c1.get_format_time())
# c1["hour"] = 11
# c1["minute"] = 24
# c1["second"] = 59
# print(c1["hour"], c1["minute"], c1["second"])

# c1 = Clock(100)
# c2 = Clock(200)
# # c4 = Clock(300)
# print(c1.get_format_time())
# print(c2.get_format_time())
# # print(c4.get_format_time())
# # c3 = c1 + c2 + c4
# # print(c3.get_format_time())
# # c1 += c2
# # print(c1.get_format_time())
#
# if c1 == c2:
#     print("Время равно")
# else:
#     print("Время не равно")
#
# if c1 != c2:
#     print("Время не равно")
# else:
#     print("Время равно")

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError("Неверный индекс")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError("Ключ должен быть целым положительным числом")
#
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)
#             self.marks.extend([None] * off)
#         self.marks[key] = value
#
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise TypeError("Ключ должен быть целым числом")
#         del self.marks[key]
#
#
# s1 = Student("Сергей", [5, 5, 3, 4, 5])
# print(s1.marks[2])
# print(s1[2])
# s1[10] = 4
# del s1[2]
# print(s1.marks)

# from random import choice, randint
#
#
# class Cat:
#     def __init__(self, name, age, pol):
#         self.name = name
#         self.age = age
#         self.pol = pol
#
#     def __str__(self):
#         if self.pol == "M":
#             return f"{self.name} is good boy!!!"
#         elif self.pol == "F":
#             return f"{self.name} is good girl!!!"
#         else:
#             return f"{self.name} Хороший котёнок!!!"
#
#     def __repr__(self):
#         return f"Cat(name = '{self.name}', age = {self.age}, pol = {self.pol})"
#
#     def __add__(self, other):
#         if self.pol != other.pol:
#             return [Cat("No name", 0, choice(["M", "F"])) for _ in range(randint(1, 5))]
#         else:
#             raise TypeError("Types are not supported")
#
#
# cat1 = Cat("Tom", 4, "M")
# cat2 = Cat("Elsa", 5, "F")
# cat3 = Cat("Murzik", 3, "M")
# print(cat1)
# print(cat2)
# print(cat1 + cat3)


#                                               Полиморфизм

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_perimeter(self):
#         return 2 * (self.width + self.height)
#
#
# class Square:
#     def __init__(self, length):
#         self.length = length
#
#     def get_perimeter(self):
#         return 4 * self.length
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimeter(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
#
# s1 = Square(10)
# s2 = Square(20)
#
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
#
# for i in shape:
#     print(i.get_perimeter())

# class Cat:
#     def __init__(self, name, age):
#         self.age = age
#         self.name = name
#
#     def info(self):
#         return f"Я кот. Меня зовут {self.name}. Мой возраст {self.age}"
#
#     def make_sound(self):
#         return f"{self.name} мяукает"
#
#
# class Dog:
#     def __init__(self, name, age):
#         self.age = age
#         self.name = name
#
#     def info(self):
#         return f"Я Собака. Меня зовут {self.name}. Мой возраст {self.age}"
#
#     def make_sound(self):
#         return f"{self.name} гавкает"
#
#
# cat1 = Cat("Пушок", 2.5)
# dog1 = Dog("Мухтар", 4)
#
# for animal in (cat1, dog1):
#     print(animal.info())
#     print(animal.make_sound())


# class Human:
#
#     def __init__(self, last_name, first_name, age):
#         self.last_name = last_name
#         self.first_name = first_name
#         self.age = age
#
#     def info(self):
#         print(f"\n{self.last_name} {self.first_name} {self.age}", end=" ")
#
#
# class Student(Human):
#
#     def __init__(self, last_name, first_name, age, speciality, group, rating):
#         super().__init__(last_name, first_name, age)
#         self.speciality = speciality
#         self.group = group
#         self.rating = rating
#
#     def info(self):
#         super().info()
#         print(f"{self.speciality} {self.group} {self.rating}", end=" ")
#
#
# class Teacher(Human):
#
#     def __init__(self, last_name, first_name, age, speciality, experience):
#         super().__init__(last_name, first_name, age)
#         self.speciality = speciality
#         self.experience = experience
#
#     def info(self):
#         super().info()
#         print(f"{self.speciality} {self.experience}", end=" ")
#
#
# class Graduate(Student):
#
#     def __init__(self, last_name, first_name, age, speciality, group, rating, topic):
#         super().__init__(last_name, first_name, age, speciality, group, rating)
#         self.topic = topic
#
#     def info(self):
#         super().info()
#         print(f"{self.topic}", end=" ")
#
#
# group = [
#     Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
#     Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
#     Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
#     Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
#     Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
#     Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
# ]
# for i in group:
#     i.info()

#                                                   Функторы

# class Counter:
#
#     def __init__(self):
#         self.__count = 0
#
#     def __call__(self):
#         self.__count += 1
#         print(self.__count)
#
#
# c1 = Counter()
# c1()
# c1()
# c1()
# c1()

# def string_strip(chars):
#     def wrapper(string):
#         if not isinstance(string, str):
#             raise TypeError("Аргумент должен быть строкой")
#         return string.strip(chars)
#
#     return wrapper
#
#
# s1 = string_strip("!@#$%^&*()_+=- ")
# print(s1(" Hello World! "))
#
#
# class StripChars:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     # def __call__(self, string):
#     #     if not isinstance(string, str):
#     #         raise TypeError("Аргумент должен быть строкой")
#     #     return string.strip(self.__chars)
#
#     def __call__(self, *args):
#         if not isinstance(args[0], str):
#             raise TypeError("Аргумент должен быть строкой")
#         return args[0].strip(self.__chars)
#
#
# s2 = StripChars("!@#$%^&*()_+=- ")
# print(s2(" Hello World! "))

#                                                   Класс как декоратор

# class MyDecorator:
#
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self):
#         print("До вызова функции")
#         self.func()
#         print("После вызова функции")
#
#
# @MyDecorator
# def func_test():
#     print("Hello, I am func 'func_test'")
#
#
# func_test()


# class MyDecorator:
#
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, x, y):
#         # print("До вызова функции")
#         # self.func(x, y)
#         # print("После вызова функции")
#         return f"Перед вызовом функции\n{self.func(x, y)}\nПосле вызова функции"
#
#
# @MyDecorator
# def func_test(a, b):
#     return a * b
#
#
# print(func_test(5, 6))

# class Power:
#
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args):
#         return f"Результат: {self.func(*args) ** 2}"
#
#
# @Power
# def func_test(a, b):
#     return a * b
#
#
# print(func_test(2, 3))

# class MyDecorator:
#
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         return f"Перед вызовом функции\n{self.func(*args, **kwargs)}\nПосле вызова функции"
#
#
# @MyDecorator
# def func_test(a, b):
#     return a * b
#
#
# @MyDecorator
# def func_test1(a, b, c):
#     return a * b * c
#
#
# print(func_test(5, 6))
# print(func_test1(2, c=5, b=2))


# class MyDecorator:
#
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __call__(self, fn):
#         def wrapper(*args, **kwargs):
#             return f"Перед вызовом функции\n{self.arg} {args[0]} * {args[1]} = {fn(*args, **kwargs)}\nПосле вызова функции"
#
#         return wrapper
#
#
# @MyDecorator("Произведение:")
# def func_test(a, b):
#     return a * b
#
#
# print(func_test(5, 6))

# class Power:
#
#     def __init__(self, power):
#         self.power = power
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             return f"Результат: {func(*args, **kwargs) ** self.power}"
#         return wrapper
#
#
# @Power(3)
# def func_test(a, b):
#     return a * b
#
#
# print(func_test(2, 2))
# print(func_test(b=2, a=2))


# def dec(fn):
#     def wrapper(*args, **kwargs):
#         print("*" * 20)
#         fn(*args, **kwargs)
#         print("*" * 20)
#
#     return wrapper
#
#
# class Person:
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @dec
#     def info(self):
#         print(self.name, self.surname)
#
#
# p = Person("Вася", "Петров")
# p.info()

# def decorator(cls):
#     class Wrapper(cls):
#         def doubler(self, value):
#             return value * 2
#
#     return Wrapper
#
#
# @decorator
# class ActualClass:
#
#     def __init__(self):
#         print("Инициализация ActualClass")
#
#     def quad(self, value):
#         return value * 4
#
#
# obj = ActualClass()
# print(obj.quad(5))
# print(obj.doubler(5))

#                                                 Дескриптор

# class String:
#     def __init__(self, value=None):
#         if value:
#             self.set(value)
#
#     def get(self):
#         return self.__value
#
#     def set(self, value):
#         if not isinstance(value, str):
#             raise ValueError("Ожидается строка")
#         self.__value = value
#
#
# class Person:
#
#     def __init__(self, name, surname):
#         self.name = String(name)
#         self.surname = String(surname)
#
#     # @property
#     # def name(self):
#     #     return self.__name
#     #
#     # @property
#     # def surname(self):
#     #     return self.__surname
#     #
#     # @name.setter
#     # def name(self, value):
#     #     if not isinstance(value, str):
#     #         raise ValueError("Имя должно быть строкой")
#     #     self.__name = value
#     #
#     # @surname.setter
#     # def surname(self, value):
#     #     if not isinstance(value, str):
#     #         raise ValueError("Имя должно быть строкой")
#     #     self.__surname = value
#     #
#     # @name.deleter
#     # def name(self):
#     #     del self.__name
#     #
#     # @surname.deleter
#     # def surname(self):
#     #     del self.__surname
#
#
# p = Person("Вася", "Петров")
# p.name.set("Игорь")


# class ValidString:
#
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError("Ожидается строка")
#         instance.__dict__[self.__name] = value
#
#
# class Person:
#
#     name = ValidString()
#     surname = ValidString()
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#
# p = Person("Вася", "Петров")
#
# print(p.name)
# print(p.surname)


# class NonNegative:
#
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         # return instance.__dict__[self.name]
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError("Значение должно быть в диапазоне от 0 до 100")
#         # instance.__dict__[self.name] = value
#         setattr(instance, self.name, value)
#
#
# class Order:
#     prise = NonNegative()
#     quantity = NonNegative()
#
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def total(self):
#         return self.price * self.quantity
#
#
# apple_order = Order("apple", 5, 10)
# apple_order.quantity = 15
# print(apple_order.price)
# print(apple_order.total())
# print(apple_order.__dict__)


#                                                 Метаклассы

# a = 5
# print(type(a))
# print(type(int))

# MyList = type(
#     "MyList",
#     (list,),
#     dict(get_length=lambda self: len(self)
#          ))
#
# lst = MyList()
# lst.append(5)
# lst.append(7)
# print(lst, lst.get_length())

#                                           Создание модулей

# import geometry.rect
# import geometry.sq
# import geometry.trian

# from geometry import rect, sq, trian
#
#
# def run():
#     r1 = rect.Rectangle(1, 2)
#     r2 = rect.Rectangle(3, 4)
#
#     s1 = sq.Square(10)
#     s2 = sq.Square(20)
#
#     t1 = trian.Triangle(1, 2, 3)
#     t2 = trian.Triangle(4, 5, 6)
#
#     shape = [r1, r2, s1, s2, t1, t2]
#
#     for g in shape:
#         print(g.get_perimetr())
#
#
# if __name__ == '__main__':
#     run()


# from car.electrocar import ElectroCar
#
# if __name__ == '__main__':
#     e_car = ElectroCar("Tesla", "T", 2020, 1000)
#     e_car.show_car()
#     e_car.description_battery()

# class Employee:
#     def __init__(self, kod, name):
#         self.id = kod
#         self.name = name
#
#
# class SalaryEmployee(Employee):
#     """Административные работники, имеют фиксированную зарплату"""
#
#     def __init__(self, kod, name, weekly_salary):
#         super().__init__(kod, name)
#         self.weekly_salary = weekly_salary
#
#     def calculate_payroll(self):
#         return self.weekly_salary
#
#
# class HourlyEmployee(Employee):
#     """Сотрудники с почасовой оплатой"""
#
#     def __init__(self, kod, name, hours_worked, house_rate):
#         super().__init__(kod, name)
#         self.hours_worked = hours_worked
#         self.house_rate = house_rate
#
#     def calculate_payroll(self):
#         return self.hours_worked * self.house_rate
#
#
# class CommissionEmployee(SalaryEmployee):
#     """Торговые представители, фиксированная зарплата + комиссия"""
#
#     def __init__(self, kod, name, weekly_salary, commission):
#         super().__init__(kod, name, weekly_salary)
#         self.commission = commission
#
#     def calculate_payroll(self):
#         fixed = super().calculate_payroll()
#         return fixed + self.commission
#
#
# class PayrollSystem:
#     def calculate(self, employees):
#         print("Расчет заработной платы")
#         print("=" * 50)
#         for employee in employees:
#             print(f"Заработная плата: {employee.id} - {employee.name}")
#             print(f"- Проверить сумму: {employee.calculate_payroll()}")
#             print()
#
#
# salary_employee = SalaryEmployee(1, "Валерий Задорожный", 1500)
# hourly_employee = HourlyEmployee(2, "Илья Кромин", 40, 15)
# commission_employee = CommissionEmployee(3, "Николай Хорольский", 1000, 250)
# payroll_system = PayrollSystem()
# payroll_system.calculate([
#     salary_employee,
#     hourly_employee,
#     commission_employee
# ])


#                                               Упаковка данных
#                                               Сериализация
#                                               Десериализация

import pickle

# file_name = "basket.txt"
#
# shop_list = {
#     "фрукты": ("яблоки", "манго"),
#     "овощи": ["морковь"],
#     "бюджет": 1000
# }
#
# with open(file_name, "wb") as f:
#     pickle.dump(shop_list, f)
#
# with open(file_name, "rb") as f:
#     new_shop_list = pickle.load(f)
#
# print(new_shop_list)

# class Text:
#     num = 35
#     string = 'Привет'
#     lst = [1, 2, 3]
#     tpl = (22, 23)
#
#     def __str__(self):
#         return f'Число: {self.num}\nСтрока: {self.string}\nСписок: {self.lst}\nКортеж: {self.tpl}'
#
#
# obj = Text()
# my_obg = pickle.dumps(obj)
# print(my_obg)
#
# obj2 = pickle.loads(my_obg)
# print(obj2)

# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = "test"
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f"{self.a}, {self.b}, {self.c(2)}"
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr["c"]
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
# item1 = Test2()
# print(item1)
# item2 = pickle.dumps(item1)
# item3 = pickle.loads(item2)
# print(item3)

import json

# data = {
#     "name": "Джон",
#     "age": 30,
#     20: None,
#     True: 1,
#     "hobbies": ("running", "sky diving", "singing"),
#     "children": ["Alica", "Bob"]
# }

# with open("data_file.json", "w") as f:
#     json.dump(data, f, indent=4)
#
# with open("data_file.json", "r") as f:
#     new_data = json.load(f)
#
# print(new_data)

# json_string = json.dumps(data, ensure_ascii=False)
# print(json_string)
# print(type(json_string))
#
# data2 = json.loads(json_string)
# print(data2)
# print(type(data2))

# from random import choice
#
#
# def gen_person():
#     name = ''
#     tel = ''
#
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letters)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#
#     person = {
#         'name': name,
#         'tel': tel
#     }
#
#     return person
#
#
# def write_json(person_dict):
#     try:
#         data = json.load(open('persons.json'))
#     except FileNotFoundError:
#         data = []
#
#     data.append(person_dict)
#     with open("persons.json", "w") as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
#     write_json(gen_person())

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         # a = ''
#         # for i in self.marks:
#         #     a += str(i) + ', '
#         # return f"Студент: {self.name} => {a[:-2]}"
#         a = ", ".join(map(str, self.marks))
#         return f"Студент: {self.name} => {a}"
#         # return f"Студент: {self.name} => {self.marks}"
#
#     def add_mark(self, mark):
#         self.marks.append(mark)
#
#     def del_mark(self, index):
#         self.marks.pop(index)
#
#     def edit_mark(self, index, mark):
#         self.marks[index] = mark
#
#     def average_mark(self):
#         return round(sum(self.marks) / len(self.marks), 2)
#
#     def get_file_name(self):
#         return self.name.lower() + ".json"
#
#     def dump_to_json(self):
#         data = {"name": self.name, "marks": self.marks}
#         with open(self.get_file_name(), "w") as f:
#             json.dump(data, f, indent=2)
#
#     def load_from_file(self):
#         with open(self.get_file_name(), "r") as f:
#             print(json.load(f))
#
#
# class Group:
#     def __init__(self, students, group):
#         self.students = students
#         self.group = group
#
#     def __str__(self):
#         a = '\n'.join(map(str, self.students))
#         return f"Группа: {self.group}\n{a}"
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def remove_student(self, index):
#         return self.students.pop(index)
#
#     @staticmethod
#     def change_group(gr1, gr2, index):
#         gr2.add_student(gr1.remove_student(index))
#
#     def get_file_name(self):
#         return self.group.lower().replace(" ", "-") + ".json"
#
#     def dump_to_json(self):
#         data = [
#             {'name': student.name, "marks": student.marks} for student in self.students
#         ]
#         with open(self.get_file_name(), 'w') as f:
#             json.dump(data, f, indent=2)
#
#     def load_from_file(self):
#         with open(self.get_file_name(), "r") as f:
#             print(json.load(f))
#
#     def add_db(self):
#         try:
#             data = json.load(open('db.json'))
#         except FileNotFoundError:
#             data = {}
#         js = [
#             {student.name: student.marks} for student in self.students
#         ]
#         data[self.group] = js
#         with open("db.json", "w+") as f:
#             json.dump(data, f, indent=2)
#         print(f"Группа {self.group} добавлена в файл")
#
#     @staticmethod
#     def load_groups(file):
#         with open(file, "r") as f:
#             print(json.load(f))
#
# # st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
# # print(st1)
# # st1.add_mark(4)
# # print(st1)
# # st1.del_mark(2)
# # print(st1)
# # st1.edit_mark(2, 5)
# # print(st1)
# # print(st1.average_mark())
# # st1.dump_to_json()
# # st1.load_from_file()
# # st2 = Student('Nikolaenko', [2, 3, 5, 4, 2])
# # st2.dump_to_json()
# # st2.load_from_file()
#
# st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
# st2 = Student('Nikolaenko', [2, 3, 5, 4, 2])
# st3 = Student('Birukov', [3, 5, 3, 2, 5, 4])
#
# sts1 = Group([st1, st2], "ГК Python")
# # print(sts1)
# # print()
# sts1.add_student(st3)
# # print(sts1)
# # print()
# sts1.remove_student(1)
# print(sts1)
# print()
# sts2 = Group([st2], "ГК Web")
# # print(sts2)
# print()
# Group.change_group(sts1, sts2, 0)
# print(sts1)
# print()
# print(sts2)
# print()
# sts2.dump_to_json()
# sts2.load_from_file()
#
# sts1.add_db()
# sts2.add_db()
#
# file_name = "db.json"
# Group.load_groups(file_name)


# class CountryCapital:
#
#     def load(file_name):
#         try:
#             data = json.load(open(file_name))
#         except FileNotFoundError:
#             data = {}
#         finally:
#             return data
#
#     @staticmethod
#     def add_country(file_name):
#         new_country = input("Введите название страны: ").lower()
#         new_capital = input("Введите название столицы: ").lower()
#
#         data = CountryCapital.load(file_name)
#
#         data[new_country] = new_capital
#
#         with open(file_name, "w") as f:
#             json.dump(data, f, indent=2)
#
#     @staticmethod
#     def delete_country(file_name):
#         del_country = input("Введите название страны: ").lower()
#
#         data = CountryCapital.load(file_name)
#
#         if del_country in data:
#             del data[del_country]
#
#             with open(file_name, "w") as f:
#                 json.dump(data, f, indent=2)
#         else:
#             print("Страна не найдена")
#
#     @staticmethod
#     def search_data(file_name):
#         country = input("Введите название страны: ").lower()
#
#         data = CountryCapital.load(file_name)
#
#         if country in data:
#             print(f"Страна {country.capitalize()} столица {data[country].capitalize()} есть в словаре")
#         else:
#             print(f"Страны {country.capitalize()} нет в словаре")
#
#     @staticmethod
#     def edit_data(file_name):
#         country = input("Введите название страны для корректировки: ").lower()
#
#         data = CountryCapital.load(file_name)
#
#         if country in data:
#             new_capital = input("Введите новое название столицы: ").lower()
#             data[country] = new_capital
#
#             with open(file_name, "w") as f:
#                 json.dump(data, f, indent=2)
#         else:
#             print("Страна не найдена")
#
#     @staticmethod
#     def load_from_file(file_name):
#         with open(file_name) as f:
#             print({k.capitalize(): v.capitalize() for k, v in json.load(f).items()})
#
#
# file = "list_capital.json"
#
# while True:
#     index = input("Выбор  действия\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных\n"
#                   "4 - редактирование данных\n5 - просмотр данных\n6 -завершение работы\nВвод: ")
#
#     if index == "1":
#         CountryCapital.add_country(file)
#     elif index == "2":
#         CountryCapital.delete_country(file)
#     elif index == "3":
#         CountryCapital.search_data(file)
#     elif index == "4":
#         CountryCapital.edit_data(file)
#     elif index == "5":
#         CountryCapital.load_from_file(file)
#     elif index == "6":
#         break
#     else:
#         print("Неверный ввод")


# import requests
# import json
#
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# todos = json.loads(response.text)
#
# todos_by_user = {}
#
# for todo in todos:
#     if todo["completed"]:
#         try:
#             todos_by_user[todo["userId"]] += 1
#         except KeyError:
#             todos_by_user[todo["userId"]] = 1
#
# # print(max(todos_by_user, key=todos_by_user.get), "completed", max(todos_by_user.values()))
# top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# print(top_users)
#
# max_complete = top_users[0][1]
# print(max_complete)
#
# users = []
#
# for user, num_complete in top_users:
#     if num_complete < max_complete:
#         break
#     users.append(user)
#
# max_users = " and ".join([str(user) for user in users])
# print(f"Users {max_users} completed {max_complete} Todos")
#
#
# def keep(todo):
#     completed = todo["completed"]
#     max_count = str(todo["userId"]) in users
#     return completed and max_count
#
#
# with open("filter_file.json", "w") as f:
#     filtered = list(filter(keep, todos))
#     json.dump(filtered, f, indent=4)

import csv

# with open("data2.csv") as f:
#     file_reader = csv.reader(f, delimiter=';')
#     count = 0
#
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         else:
#             print(f"\t{row[0]} {row[1]}. Родился в {row[2]} году.")
#         count += 1

# with open("data2.csv") as f:
#     file_names = ['Имя', 'Профессия', 'Год рождения']
#     file_reader = csv.DictReader(f, delimiter=";", fieldnames=file_names)
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         print(f"\t{row['Имя']} - {row['Профессия']}. Родился в {row['Год рождения']} году.")
#         count += 1

# with open("student.csv", "w") as f:
#     writer = csv.writer(f, delimiter=";", lineterminator="\r")
#     writer.writerow(["Имя", "Класс", "Возраст"])
#     writer.writerow(["Вася", 9, 15])
#     writer.writerow(["Петя", 11, 16])
#     writer.writerow(["Маша", 10, 17])
#     writer.writerow(["Оля", 10, 18])

# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
# with open("data_new.csv", "w") as f:
#     writer = csv.writer(f, delimiter=";", lineterminator="\r")
#     # for row in data:
#     #     writer.writerow(row)
#     writer.writerow(data)
#
# with open("data_new.csv") as f:
#     print(f.read())

# with open("student1.csv", "w") as f:
#     names = ["Имя", "Возраст"]
#     file_writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=names)
#     file_writer.writeheader()
#     file_writer.writerow({"Имя": "Вася", "Возраст": 15})
#     file_writer.writerow({"Имя": "Петя", "Возраст": 16})
#     file_writer.writerow({"Имя": "Маша", "Возраст": 17})
#     file_writer.writerow({"Имя": "Оля", "Возраст": 18})

# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]
#
# with open("dict_writer.csv", "w") as f:
#     writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=list(data[0].keys()))
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)

#                                           Парсинг

from bs4 import BeautifulSoup

# f = open("index.html").read()

# soup = BeautifulSoup(f, "html.parser")
# row = soup.find("div", class_="name").text
# row = soup.find_all("div", class_="name")
# row = soup.find_all("div", class_="row")[1].find("div", class_="links")
# row = soup.find_all("div", {"data-set": "salary"})
# row = soup.find("div", string="Alena").parent
# row = soup.find("div", string="Alena").find_parent(class_="row")
# row = soup.find("div", id="whois3").find_next_sibling()
# row = soup.find("div", id="whois3").find_previous_sibling()
# print(row)

# def get_copywriter(tag):
#     whois = tag.find("div", class_="whois")
#     if "Copywriter" in whois.text:
#         return tag
#     return None
#
#
# f = open("index.html").read()
# soup = BeautifulSoup(f, "html.parser")
# copywriter = []
# row = soup.find_all("div", class_="row")
# for i in row:
#     cw = get_copywriter(i)
#     if cw:
#         copywriter.append(cw)
#
# print(copywriter)

import re


def get_salary(s):
    pattern = r"\d+"
    res = re.search(pattern, s).group()
    print(res)


f = open("index.html").read()
soup = BeautifulSoup(f, "html.parser")
salary = soup.find_all("div", {"data-set": "salary"})

for i in salary:
    get_salary(i.text)
