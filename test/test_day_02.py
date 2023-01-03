import unittest

from day_02.day_02 import Day2


class TestDay2(unittest.TestCase):
    example: list[str] = [
        'A Y',
        'B X',
        'C Z',
    ]

    def test_part_1(self):
        self.assertEqual(Day2().day2_part1(self.example), 15)

    def test_part_2(self):
        self.assertEqual(Day2().day2_part2(self.example), 12)