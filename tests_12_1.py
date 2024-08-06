# -*- coding: utf-8 -*-
# tests_12_1.py
import runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        def walk_10():  # 10 calls to the "runner.Runner.walk()"
            walker1 = runner.Runner('somebody')
            for walk in range(10):
                walker1.walk()
            return walker1.distance

        # test case
        self.assertEqual(walk_10(), 50)

    def test_run(self):
        def run_10():  # 10 calls to the "runner.Runner.run()"
            walker1 = runner.Runner('somebody')
            for walk in range(10):
                walker1.run()
            return walker1.distance

        # test case
        self.assertEqual(run_10(), 100)

    def test_challenge(self):
        def walk10():  # 10 calls to the "runner.Runner.walk()"
            walker1 = runner.Runner('somebody')
            for walk in range(10):
                walker1.walk()
            return walker1.distance

        def run10():  # 10 calls to the "runner.Runner.run()"
            walker1 = runner.Runner('somebody')
            for walk in range(10):
                walker1.run()
            return walker1.distance

        # test case
        self.assertNotEqual(walk10(), run10())

print('----------- The End -----------')