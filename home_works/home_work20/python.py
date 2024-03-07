def count_negative_numbers(lst, index=0):
    if index == len(lst):
        return 0

    if lst[index] < 0:
        return 1 + count_negative_numbers(lst, index + 1)
    else:
        return count_negative_numbers(lst, index + 1)


print("Количество отрицательных чисел в массиве:", count_negative_numbers([-2, 3, 8, -11, -4, 6]))


def negative_numbers(n):
    if not n:
        return 0
    count = 0
    if n[0] < 0:
        count += 1
    return count + negative_numbers(n[1:])


lst = [-2, 3, 8, -11, -4, 6]
print(negative_numbers(lst))




