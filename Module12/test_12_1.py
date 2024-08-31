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
