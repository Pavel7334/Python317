area = 0


def parallelepiped_area(a, b, c):
    global area
    area = 2 * (a * b + a * c + b * c)

    def rectangle_area():
        s = a * b
        return s

    rectangle_area()
    return area


print(parallelepiped_area(2, 4, 6))
print(parallelepiped_area(5, 8, 2))
print(parallelepiped_area(1, 6, 8))


def parallelepiped_area():
    area = 0

    def rectangle_area(a, b, c):
        nonlocal area
        square_a_b = a * b
        square_a_c = a * c
        square_b_c = b * c
        area = 2 * (square_a_b + square_a_c + square_b_c)
        return area

    return rectangle_area


print(parallelepiped_area()(2, 4, 6))
print(parallelepiped_area()(5, 8, 2))
print(parallelepiped_area()(1, 6, 8))
