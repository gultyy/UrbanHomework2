"""
Задача:
Напишите функцию-генератор all_variants(text), которая принимает строку text и возвращает объект-генератор, при каждой
итерации которого будет возвращаться подпоследовательности переданной строки.

Пункты задачи:

    Напишите функцию-генератор all_variants(text).
    Опишите логику работы внутри функции all_variants.
    Вызовите функцию all_variants и выполните итерации.
"""


def all_variants(text):
    start = 0
    width = 1
    while True:
        variant = text[start:start + width]
        yield variant
        if width == len(text):
            break
        if start + width == len(text):
            width += 1
            start = 0
        else:
            start += 1


a = all_variants("abcde")
for i in a:
    print(i)
