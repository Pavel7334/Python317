s = []
print("Введите элементы списка: ")
for num in range(int(input("n = "))):
    x = int(input("-> "))
    s.append(x)
print("Введите индекс:")
ind = int(input("k = "))
print("Введите значение:")
val = int(input("c = "))
s.insert(ind, val)
print(s)
