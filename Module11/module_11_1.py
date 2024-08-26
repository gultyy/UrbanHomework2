"""
Задача:

    Выберите одну или несколько сторонних библиотек Python, например, requests, pandas, numpy, matplotlib, pillow.
    После выбора библиотек(-и) изучите документацию к ней(ним), ознакомьтесь с их основными возможностями и функциями.
    К каждой библиотеке дана ссылка на документацию ниже.

Если вы выбрали:

    requests - запросить данные с сайта и вывести их в консоль.
    pandas - считать данные из файла, выполнить простой анализ данных (на своё усмотрение) и вывести результаты в
    консоль.
    numpy - создать массив чисел, выполнить математические операции с массивом и вывести результаты в консоль.
    matplotlib - визуализировать данные с помощью библиотеки любым удобным для вас инструментом из библиотеки.
    pillow - обработать изображение, например, изменить его размер, применить эффекты и сохранить в другой формат.

В приложении к ссылке на GitHub напишите комментарий о возможностях, которые предоставила вам выбранная библиотека и
как вы расширили возможности Python с её помощью.
Примечания:

    Можете выбрать не более 3-х библиотек для изучения.
    Желательно продемонстрировать от 3-х функций/классов/методов/операций из каждой выбранной библиотеки.
"""

# 1
import requests

r = requests.get('https://github.com/gultyy/UrbanHomeworks/blob/master/Module9/module_9_7.py')
print(r.url)
print(r.headers)

try:
    r.json()
except:
    print(f'Сбой декодирования JSON - {r.status_code}')

r = requests.options('https://github.com/gultyy/UrbanHomeworks/blob/master/Module9/module_9_7.py')


# 2
import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])  # create 2D array
print(f'Двумерный массив:\n{a}')
print(f'Сумма массива: {a.sum()}')
ones = np.ones([2, 4], dtype=int)  # create 2D ones array
ones *= 3
a2 = a + ones
print(f'Новый двумерный массив:\n{a2}')
print(f'Сумма нового двумерного массива: {a2.sum()}')

# 3
import matplotlib.pyplot as plt

theta = np.linspace(0, 2 * np.pi, 100)

# Generating x and y data (heart)
x = 16 * (np.sin(theta) ** 3)
y = 13 * np.cos(theta) - 5 * np.cos(2 * theta) - 2 * np.cos(3 * theta) - np.cos(4 * theta)

# Plotting
plt.plot(x, y, color='red')
plt.title('I love Urban university')
plt.show()  # Show the figure.
