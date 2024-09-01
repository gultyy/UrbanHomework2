"""
Задача "Логирование бегунов":
В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
Основное обновление - выбрасывание исключений, если передан неверный тип в name и если передано отрицательное значение
в speed.

Для решения этой задачи вам понадобиться класс RunnerTest из предыдущей задачи.
В модуле tests_12_4.py импортируйте пакет logging и настройте basicConfig на следующие параметры:

    Уровень - INFO
    Режим - запись с заменой('w')
    Название файла - runner_tests.log
    Кодировка - UTF-8
    Формат вывода - на своё усмотрение, обязательная информация: уровень логирования, сообщение логирования.


Дополните методы тестирования в классе RunnerTest следующим образом:
test_walk:

    Оберните основной код конструкцией try-except.
    При создании объекта Runner передавайте отрицательное значение в speed.
    В блок try добавьте логирование INFO с сообщением '"test_walk" выполнен успешно'
    В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING с сообщением
    "Неверная скорость для Runner".

test_run:

    Оберните основной код конструкцией try-except.
    При создании объекта Runner передавайте что-то кроме строки в name.
    В блок try добавьте логирование INFO с сообщением '"test_run" выполнен успешно'
    В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING с сообщением
    "Неверный тип данных для объекта Runner".
"""
import logging
import unittest
from HumanMoveTest import rt_with_exceptions as rt


class RunnerTest(unittest.TestCase):
    is_frozen = False

    # @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            runner_ = rt.Runner('Alex', -55)
            for i in range(10):
                runner_.walk()
            self.assertEqual(runner_.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    # @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            runner_ = rt.Runner(183)
            for i in range(10):
                runner_.run()
            self.assertEqual(runner_.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    # @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    # def test_challenge(self):
    #     runners = [rt.Runner(f'runner{i}', i) for i in range(2)]
    #     for i in range(10):
    #         runners[0].run()
    #         runners[1].walk()
    #     self.assertNotEqual(runners[0].distance, runners[1].distance)


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                        format='%(asctime)s | %(levelname)s | %(message)s')

if __name__ == '__main__':
    unittest.main()