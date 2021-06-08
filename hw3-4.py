"""
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


# Первый вариант: **
def my_func(x, y):
    x, y = float(x), int(y)
    return x ** y


print(my_func(2, -4))


# Второй вариант: цикл
def my_func(x, y):
    x, y = float(x), int(y)
    res = x
    for i in range(abs(y) - 1):
        res *= x
    return 1 / res


print(my_func(2, -4))
