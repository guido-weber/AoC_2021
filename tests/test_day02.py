import unittest

from aoc_2021 import day02

input = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""


class TestDay02(unittest.TestCase):
    def test_day02_1(self):
        self.assertEqual(day02.day02_1(input), 150)

    def test_day02_2(self):
        self.assertEqual(day02.day02_2(input), 900)
