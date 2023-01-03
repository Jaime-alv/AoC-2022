import unittest

from day_01 import day_01 as d

class TestDay1(unittest.TestCase):
    example = [
        "1000",
        "2000",
        "3000",
        "",
        "4000",
        "",
        "5000",
        "6000",
        "",
        "7000",
        "8000",
        "9000",
        "",
        "10000",
        ""
    ]

    def test_splits(self):
        self.assertEqual(d.sum_splits([1, 2, 3]), 6)

    def test_iterate(self):
        self.assertListEqual(d.iterate_list(self.example),
                             sorted([6000, 4000, 11000, 24000, 10000]))

    def test_max(self):
        self.assertEqual(d.find_max([6000, 4000, 11000, 24000, 10000]), 24000)

    def test_part1(self):
        self.assertEqual(d.process_part_1(self.example), 24000)

    def test_part2(self):
        self.assertEqual(d.process_part_2(self.example), 45000)