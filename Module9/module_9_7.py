"""
Задание: Декораторы в Python

Цель задания:
Освоить механизмы создания декораторов Python.
Практически применить знания, создав функцию декоратор и обернув ею другую функцию.

Задание:
Напишите 2 функции:

    Функция, которая складывает 3 числа (sum_three)
    Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и
    "Составное" в противном случае.
"""


def is_prime(func):
    def wrapper(a, b, c):
        n = func(a, b, c)
        d = 2
        while n % d != 0:
            d += 1
        if d == n:
            print("Простое")
        else:
            print("Составное")
        return n
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


print(sum_three(2, 3, 6))
print(sum_three(10, 9, 4))
print(sum_three(50, 30, 20))
print(sum_three(2, 1, 1))
