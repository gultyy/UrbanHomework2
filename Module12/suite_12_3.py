"""
Часть 1. TestSuit.

    Создайте модуль suite_12_3.py для описания объекта TestSuite. Укажите на него переменной с произвольным названием.
    Добавьте тесты RunnerTest и TournamentTest в этот TestSuit.
    Создайте объект класса TextTestRunner, с аргументом verbosity=2.
"""
import unittest
from tests_12_3 import RunnerTest
from tests_12_3 import TournamentTest

runST = unittest.TestSuite()
runST.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
runST.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runST)
