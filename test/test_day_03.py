
import unittest

from day_03 import day_03 as d


class TestDay3(unittest.TestCase):
    example: list[str] = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw"
    ]

    def test_divide(self):
        self.assertEqual(d.divide('vJrwpWtwJgWrhcsFMMfFFhFp'),
                         ('vJrwpWtwJgWr', 'hcsFMMfFFhFp'))
        self.assertEqual(d.divide('jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL'),
                         ('jqHRNqRjqzjGDLGL', 'rsFMfFZSrLrFZsSL'))

    def test_filter_char(self):
        self.assertEqual(d.filter_string(
            ('vJrwpWtwJgWr', 'hcsFMMfFFhFp')), "p")
        self.assertEqual(d.filter_string(
            d.divide("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL")), "L")

    def test_find_index(self):
        self.assertEqual(d.find_by_index("p"), 16)
        self.assertEqual(d.find_by_index("L"), 38)
        self.assertEqual(d.find_by_index("v"), 22)
        self.assertEqual(d.find_by_index("r"), 18)
        self.assertEqual(d.find_by_index("Z"), 52)

    def test_example(self):
        self.assertEqual(d.add_items(self.example), 157)

    def test_split(self):
        self.assertEqual(d.split_in_groups(self.example), [("vJrwpWtwJgWrhcsFMMfFFhFp",
                                                            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
                                                            "PmmdzqPrVvPwwTWBwg"),
                                                           ("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
                                                            "ttgJtRGJQctTZtZT",
                                                            "CrZsJsPPZsGzwwsLwLmpwMDw")])

    def test_rucksacks(self):
        self.assertEqual(d.element_in_all_rucksack(("vJrwpWtwJgWrhcsFMMfFFhFp",
                                                    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
                                                    "PmmdzqPrVvPwwTWBwg")), "r")
        self.assertEqual(d.element_in_all_rucksack(("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
                                                    "ttgJtRGJQctTZtZT",
                                                    "CrZsJsPPZsGzwwsLwLmpwMDw")), "Z")
