a = int(input("Укажите кол-во символов: "))
b = input("Укажите тип символов: ")
c = int(input("Укажите ориентацию линии 0 или 1: "))
while a:
    if c == 0:
        print(b, end=" ")
        a -= 1
    elif c == 1:
        print(b)
        a -= 1


