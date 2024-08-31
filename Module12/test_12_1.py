"""
Задача "Проверка на выносливость":

Напишите класс RunnerTest, наследуемый от TestCase из модуля unittest. В классе пропишите следующие методы:

    test_walk - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод walk у этого
     объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 50.
    test_run - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод run у этого
    объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 100.
    test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами. Далее 10 раз у объектов
    вызываются методы run и walk соответственно. Т.к. дистанции должны быть разными, используйте метод assertNotEqual,
    чтобы убедится в неравенстве результатов.

Запустите кейс RunnerTest. В конечном итоге все 3 теста должны пройти проверку.

"""

import unittest
from HumanMoveTest import runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner_ = runner.Runner('runner')
        for i in range(10):
            runner_.walk()
        self.assertEqual(runner_.distance, 50)

    def test_run(self):
        runner_ = runner.Runner('runner')
        for i in range(10):
            runner_.run()
        self.assertEqual(runner_.distance, 100)

    def test_challenge(self):
        runners = [runner.Runner(f'runner{i}') for i in range(2)]
        for i in range(10):
            runners[0].run()
            runners[1].walk()
        self.assertNotEqual(runners[0].distance, runners[1].distance)


if __name__ == '__main__':
    unittest.main()
