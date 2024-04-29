def fibocacci():
    first = 1
    second = 1
    while True:
        yield first
        first, second = second, first + second


gen_obj = fibocacci()
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
