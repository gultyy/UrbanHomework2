"""
Задача "Вызов разом":
Напишите функцию apply_all_func(int_list, *functions), которая принимает параметры:

    int_list - список из чисел (int, float)
    *functions - неограниченное кол-во функций (которые применимы к спискам, состоящим из чисел)

Эта функция должна:

    Вызвать каждую функцию к переданному списку int_list
    Возвращать словарь, где ключом будет название вызванной функции, а значением - её результат работы со списком
    int_list.

Пункты задачи:

    В функции apply_all_func создайте пустой словарь results.
    Переберите все функции из *functions.
    При переборе функций записывайте в словарь results результат работы этой функции под ключом её названия.
    Верните словарь results.
    Запустите функцию apply_all_func, передав в неё список из чисел и набор других функций.
"""


def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        results[func.__name__] = func(int_list)
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
