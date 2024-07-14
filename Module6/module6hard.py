"""
Задание "Они все так похожи":
2D? 3D? Даже 4D?.... Настолько глубоко мы заходить конечно же не будем, 4D подождёт, но вот с двумерными и трёхмерными
фигурами можем поэкспериментировать.
Вы когда-нибудь задумывались как устроены графические библиотеки для языков программирования?
Безусловно, там выполняются огромные расчёты при помощи вашей видеокарты, но... Что лежит в основе удобного
использования таких объектов?

По названию задачи можно понять, что все геометрические фигуры обладают схожими свойствами, такими как: длины сторон,
цвет и др.

Давайте попробуем реализовать простейшие классы для некоторых таких фигур и при этом применить наследование (в будущем,
изучая сторонние библиотеки, вы будете замечать схожие классы, уже написанные кем-то ранее):

Общее ТЗ:
Реализовать классы Figure(родительский), Circle, Triangle и Cube, объекты которых будут обладать методами изменения
размеров, цвета и т.д.
Многие атрибуты и методы должны быть инкапсулированны и для них должны быть написаны интерфейсы взаимодействия (методы)
- геттеры и сеттеры.

Подробное ТЗ:

Атрибуты класса Figure: sides_count = 0
Каждый объект класса Figure должен обладать следующими атрибутами:

    Атрибуты(инкапсулированные): __sides(список сторон (целые числа)), __color(список цветов в формате RGB)
    Атрибуты(публичные): filled(закрашенный, bool)

И методами:

    Метод get_color, возвращает список RGB цветов.
    Метод __is_valid_color - служебный, принимает параметры r, g, b, который проверяет корректность переданных значений
    перед установкой нового цвета. Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255
    (включительно).
    Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения,
    предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.
    Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, возвращает True если все стороны целые
    положительные числа и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.
    Метод get_sides должен возвращать значение я атрибута __sides.
    Метод __len__ должен возвращать периметр фигуры.


Атрибуты класса Circle: sides_count = 1
Каждый объект класса Circle должен обладать следующими атрибутами и методами:

    Все атрибуты и методы класса Figure
    Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
    Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).


Атрибуты класса Triangle: sides_count = 3
Каждый объект класса Triangle должен обладать следующими атрибутами и методами:

    Все атрибуты и методы класса Figure
    Атрибут __height, высота треугольника (можно рассчитать зная все стороны треугольника)
    Метод get_square возвращает площадь треугольника.

Атрибуты класса Cube: sides_count = 12
Каждый объект класса Cube должен обладать следующими атрибутами и методами:

    Все атрибуты и методы класса Figure.
    Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
    Метод get_volume, возвращает объём куба.


ВАЖНО!
При создании объектов делайте проверку на количество переданных сторон, если сторон не ровно sides_count, то создать
массив с единичными сторонами и в том кол-ве, которое требует фигура.
Пример 1: Circle((200, 200, 100), 10, 15, 6), т.к. сторона у круга всего 1, то его стороны будут - [1]
Пример 2: Triangle((200, 200, 100), 10, 6), т.к. сторон у треугольника 3, то его стороны будут - [1, 1, 1]
Пример 3: Cube((200, 200, 100), 9), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [9, 9, 9, ....., 9] (12)
Пример 4: Cube((200, 200, 100), 9, 12), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [1, 1, 1, ....., 1]
"""

import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = []
        if self.__is_valid_sides(*sides):
            for count in range(len(sides)):
                self.__sides.append(sides[count])
        elif len(sides) == 1:
            for i in range(self.sides_count):
                self.__sides.append(sides[0])
        else:
            for i in range(self.sides_count):
                self.__sides[i] = 1
        self.__color = color
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            color = [r, g, b]
            self.__color = color
            # self.__color[0] = r
            # self.__color[1] = g
            # self.__color[2] = b

    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, *sides):
        for side in sides:
            if side > 0 and isinstance(side, int):
                continue
            else:
                return False
        if self.sides_count == len(sides):
            return True
        return False

    def set_sides(self, *sides):
        if self.__is_valid_sides(*sides):
            for count in range(len(sides)):
                self.__sides[count] = sides[count]


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = sides[0]/(2*math.pi)

    def get_square(self):
        return math.pi * self.__radius**2

    def get_radius(self):
        return self.__radius

    def __len__(self):
        return self.get_sides()[0]


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        sides = self.get_sides()
        a = sides[0]
        b = sides[1]
        c = sides[2]
        p = (a + b + c) / 2
        self.__height = 2 * math.sqrt(p*(p-a)*(p-b)*(p-c)) / a

    def get_square(self):
        sides = self.get_sides()
        a = sides[0]
        h = self.__height
        return a * h / 2

    def __len__(self):
        a = self.__sides[0]
        b = self.__sides[1]
        c = self.__sides[2]
        return a + b + c


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        self.__sides = []
        if 1 == len(sides):
            for i in range(Cube.sides_count):
                self.__sides.append(sides[0])
            super().__init__(color, *([sides[0]] * self.sides_count))
        else:
            for i in range(Cube.sides_count):
                self.__sides.append(1)
            super().__init__(color, *([self.__sides[0]] * self.sides_count))

    def get_volume(self):
        return self.__sides[0]**3

    def set_sides(self, *sides):
        if 1 == len(sides):
            super().set_sides(*([sides[0]] * self.sides_count))

    # def get_sides(self):
    #     return self.__sides


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
