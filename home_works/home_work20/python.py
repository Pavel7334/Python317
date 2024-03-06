def count_negative_numbers(lst, index=0):
    if index == len(lst):
        return 0

    if lst[index] < 0:
        return 1 + count_negative_numbers(lst, index + 1)
    else:
        return count_negative_numbers(lst, index + 1)


print("Количество отрицательных чисел в массиве:", count_negative_numbers([-2, 3, 8, -11, -4, 6]))
