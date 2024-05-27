"""
1.Функция с параметрами по умолчанию:

    Создайте функцию print_params(a = 1, b = 'строка', c = True), которая принимает три параметра со значениями по
    умолчанию (например сейчас это: 1, 'строка', True).
    Функция должна выводить эти параметры.
    Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
    Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])

2.Распаковка параметров:

    Создайте список values_list с тремя элементами разных типов.
    Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params, и значениями разных
    типов.
    Передайте values_list и values_dict в функцию print_params, используя распаковку параметров (* для списка и ** для
    словаря).

3.Распаковка + отдельные параметры:

    Создайте список values_list_2 с двумя элементами разных типов
    Проверьте, работает ли print_params(*values_list_2, 42)
"""


# 1
def print_params(a=11, b='String', c=False):
    print(a, b, c)


print_params()
print_params(22)
print_params(33, 'String2')
print_params(44, 'String3', True)
print_params(b = 25)
print_params(c = [1,2,3])

# 2
values_list = [25, 'Twenty_five', True]
values_dict = {'a': 26, 'b': 'Twenty_six', 'c': False}
print_params(*values_list)
print_params(**values_dict)

# 3
values_list_2 = [True, 'String']
print_params(*values_list_2, 42)
