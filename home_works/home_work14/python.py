# area = 0
#
#
# def parallelepiped_area(a, b, c):
#     global area
#     area = 2 * (a * b + a * c + b * c)
#
#     def rectangle_area():
#         s = a * b
#         return s
#
#     rectangle_area()
#     return area
#
#
# print(parallelepiped_area(2, 4, 6))
# print(parallelepiped_area(5, 8, 2))
# print(parallelepiped_area(1, 6, 8))
#
#
# def parallelepiped_area():
#     area = 0
#
#     def rectangle_area(a, b, c):
#         nonlocal area
#         square_a_b = a * b
#         square_a_c = a * c
#         square_b_c = b * c
#         area = 2 * (square_a_b + square_a_c + square_b_c)
#         return area
#
#     return rectangle_area
#
#
# print(parallelepiped_area()(2, 4, 6))
# print(parallelepiped_area()(5, 8, 2))
# print(parallelepiped_area()(1, 6, 8))


def outer(a, b, c):
    def inner(i, j):
        return i * j

    s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
    return s


print(outer(2, 4, 6))
print(outer(5, 8, 2))
print(outer(1, 6, 8))

s = 0


def outer(a, b, c):
    def inner(i, j):
        return i * j

    global s
    s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
    return s


print(s)
outer(2, 4, 6)
print(s)
outer(5, 8, 2)
print(s)
outer(1, 6, 8)
print(s)


def outer(a, b, c):  # 2, 4, 6
    s = 0  # 44

    def inner(i, j):
        nonlocal s
        s = s + i * j  # s += i * j   # s = 20 + 24 = 44

    inner(a, b)  # 2, 4
    inner(a, c)  # 2, 6
    inner(b, c)  # 4, 6
    return 2 * s  # 2 * 44


print(outer(2, 4, 6))
print(outer(5, 8, 2))
print(outer(1, 6, 8))