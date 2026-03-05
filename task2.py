import math
def plus(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Аргументы должны быть числами")
    return a + b
def minus(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Аргументы должны быть числами")
    return a - b
def multiplier(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Аргументы должны быть числами")
    return a * b
def divider(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Аргументы должны быть числами")
    if b == 0:
        raise ValueError("Делить на ноль нельзя")
    return a / b
def power(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Аргументы должны быть числами")
    return a ** b
def factorial(n):
    if not isinstance(n, int):
        raise TypeError("Факториал вычисляется только для целых чисел")
    if n < 0:
        raise ValueError("Факториала отрицательного числа не существует")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
def cosine(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Аргумент должен быть числом")
    result = math.cos(math.radians(x))
    return round(result, 10)
def average(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Аргумент должен быть списком")
    if len(numbers) == 0:
        raise ValueError("Список не может быть пустым")
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise TypeError("Все элементы списка должны быть числами")
    return sum(numbers) / len(numbers)
print("Доступные операции:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")
print("5. Возведение в степень")
print("6. Факториал")
print("7. Косинус")
print("8. Среднее арифметическое")
print("-" * 20)
while True:
    operation = input("Операция: ")
    if operation.lower() == "exit":
        print("Конец программы")
        break
    try:
        if operation == "1":
            a = float(input("Слагаемое 1: "))
            b = float(input("Слагаемое 2: "))
            result = plus(a, b)
            print(f">>> {result}")
        elif operation == "2":
            a = float(input("Уменьшаемое: "))
            b = float(input("Вычитаемое: "))
            result = minus(a, b)
            print(f">>> {result}")
        elif operation == "3":
            a = float(input("Множитель 1: "))
            b = float(input("Множитель 2: "))
            result = multiplier(a, b)
            print(f">>> {result}")
        elif operation == "4":
            a = float(input("Делимое: "))
            b = float(input("Делитель: "))
            result = divider(a, b)
            print(f">>> {result}")
        elif operation == "5":
            a = float(input("Основание: "))
            b = float(input("Показатель степени: "))
            result = power(a, b)
            print(f">>> {result}")
        elif operation == "6":
            n = int(input("Число: "))
            result = factorial(n)
            print(f">>> {result}")
        elif operation == "7":
            x = float(input("Угол в градусах: "))
            result = cosine(x)
            print(f">>> {result}")
        elif operation == "8":
            nums_input = input("Введите список чисел (через пробел): ")
            nums_list = [float(x) for x in nums_input.split()]
            result = average(nums_list)
            print(f">>> {result}")
        else:
            print("Неизвестная операция")
            continue
    except ValueError as e:
        print(f"Ошибка значения: {e}")
    except TypeError as e:
        print(f"Ошибка типа: {e}")
    except Exception as e:
        print(f"Ошибка: {e}")
    print("-" * 20)