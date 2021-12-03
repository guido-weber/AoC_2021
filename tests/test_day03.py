import unittest

from aoc_2021 import day03

input = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""


class TestDay03(unittest.TestCase):
    def test_day03_1(self):
        self.assertEqual(day03.day03_1(input), 198)
        # 2743844

    def test_day03_2(self):
        self.assertEqual(day03.day03_2(input), 230)
        # 6677951
