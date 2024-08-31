import unittest
from HumanMoveTest import runner_and_tournament as rt
from HumanMoveTest import runner


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner_ = runner.Runner('runner')
        for i in range(10):
            runner_.walk()
        self.assertEqual(runner_.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner_ = runner.Runner('runner')
        for i in range(10):
            runner_.run()
        self.assertEqual(runner_.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runners = [runner.Runner(f'runner{i}') for i in range(2)]
        for i in range(10):
            runners[0].run()
            runners[1].walk()
        self.assertNotEqual(runners[0].distance, runners[1].distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        r = {'Усэйн': 10, 'Андрей': 9, 'Ник': 3}
        self.runners = [rt.Runner(name, speed) for name, speed in r.items()]

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament1(self):
        t = rt.Tournament(90, self.runners[0], self.runners[2])
        res = t.start()
        self.all_results.append(res)
        self.assertTrue(res[max(res.keys())] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament2(self):
        t = rt.Tournament(90, self.runners[1], self.runners[2])
        res = t.start()
        self.all_results.append(res)
        self.assertTrue(res[max(res.keys())] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
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
