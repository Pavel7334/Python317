numbers = [4.3, 8.2, 2.8, 6.6, 1.5, 9.3, 5.7]


min_num = numbers[0]
for num in numbers:
    if num < min_num:
        min_num = num


max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num

summa_num = 0
for num in numbers:
    summa_num += num


print("Среднее арифметическое: ", round(summa_num/len(numbers), 2))
print("Минимальное число: ", min_num)
print("Максимальное число: ", max_num)