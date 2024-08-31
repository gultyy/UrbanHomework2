"""
Задача:
В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
В этом коде сможете обнаружить дополненный с предыдущей задачи класс Runner и новый класс Tournament.
Изменения в классе Runner:

    Появился атрибут speed для определения скорости бегуна.
    Метод __eq__ для сравнивания имён бегунов.
    Переопределены методы run и walk, теперь изменение дистанции зависит от скорости.

Класс Tournament представляет собой класс соревнований, где есть дистанция, которую нужно пробежать и список участников.
Также присутствует метод start, который реализует логику бега по предложенной дистанции.

Напишите класс TournamentTest, наследованный от TestCase. В нём реализуйте следующие методы:

setUpClass - метод, где создаётся атрибут класса all_results. Это словарь в который будут сохраняться результаты всех
тестов.
setUp - метод, где создаются 3 объекта:

    Бегун по имени Усэйн, со скоростью 10.
    Бегун по имени Андрей, со скоростью 9.
    Бегун по имени Ник, со скоростью 3.

tearDownClass - метод, где выводятся all_results по очереди в столбец.

Так же методы тестирования забегов, в которых создаётся объект Tournament на дистанцию 90. У объекта класса Tournament
запускается метод start, который возвращает словарь в переменную all_results. В конце вызывается метод assertTrue,
в котором сравниваются последний объект из all_results (брать по наибольшему ключу) и предполагаемое имя последнего
бегуна.
Напишите 3 таких метода, где в забегах участвуют (порядок передачи в объект Tournament соблюсти):

    Усэйн и Ник
    Андрей и Ник
    Усэйн, Андрей и Ник.

Как можно понять: Ник всегда должен быть последним.

Дополнительно (не обязательно, не влияет на зачёт):
В данной задаче, а именно в методе start класса Tournament, допущена логическая ошибка. В результате его работы бегун с
меньшей скоростью может пробежать некоторые дистанции быстрее, чем бегун с большей.
Попробуйте решить эту проблему и обложить дополнительными тестами.
"""
import unittest
from HumanMoveTest import runner_and_tournament as rt


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        r = {'Усэйн': 10, 'Андрей': 9, 'Ник': 3}
        self.runners = [rt.Runner(name, speed) for name, speed in r.items()]

    def test_tournament1(self):
        t = rt.Tournament(90, self.runners[0], self.runners[2])
        res = t.start()
        self.all_results.append(res)
        self.assertTrue(res[max(res.keys())] == 'Ник')

    def test_tournament2(self):
        t = rt.Tournament(90, self.runners[1], self.runners[2])
        res = t.start()
        self.all_results.append(res)
        self.assertTrue(res[max(res.keys())] == 'Ник')

    def test_tournament3(self):
        t = rt.Tournament(90, self.runners[0], self.runners[1], self.runners[2])
        res = t.start()
        self.all_results.append(res)
        self.assertTrue(res[max(res.keys())] == 'Ник')

    @classmethod
    def tearDownClass(cls):
        for res in cls.all_results:
            for i in res:
                print(f'{i}: {res[i]}', end='')
                if i != len(res):
                    print(', ', end='')
            print('')


if __name__ == '__main__':
    unittest.main()


