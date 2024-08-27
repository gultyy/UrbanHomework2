"""
Задание:
Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и проводит интроспекцию этого
объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.

1. Создайте функцию introspection_info(obj), которая принимает объект obj.
2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
  - Тип объекта.
  - Атрибуты объекта.
  - Методы объекта.
  - Модуль, к которому объект принадлежит.
  - Другие интересные свойства объекта, учитывая его тип (по желанию).
"""


def introspection_info(obj):
    obj_info = {'type': type(obj).__name__,
                'attributes': [attr_name for attr_name in dir(obj) if not callable(getattr(obj, attr_name))],
                'methods': [attr_name for attr_name in dir(obj) if callable(getattr(obj, attr_name))],
                'module': obj.__class__.__module__}
    return obj_info


class MyClass:
    def __init__(self):
        self.attr = 1
        self.attr2 = '2'

    def my_class_method(self):
        pass


my_class_instance = MyClass()
print(f'Объект класса: {introspection_info(my_class_instance)}')
print(f'Класс: {introspection_info(MyClass)}')
print(f'Число: {introspection_info(1)}')
print(f'Строка: {introspection_info("1")}')
