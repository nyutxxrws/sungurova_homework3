def mlist(elements: list, multiplier: int = 2) -> list:
    res = []
    for item in elements:
        res.append(item * multiplier)
    return res
l = input("Введите список чисел через пробел: ")
numbers = [int(x) for x in l.split()]
mult = input("Введите множитель (по умолчанию 2): ")
if mult == "":
    mult = 2
else:
    mult = int(mult)
res1 = mlist(numbers, mult)
print(f"Результат (функция): {res1}")
res2 = list(map(lambda x: x * mult, numbers))
print(f"Результат (лямбда-функция): {res2}")